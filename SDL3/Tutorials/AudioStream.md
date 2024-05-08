# Using SDL_AudioStream

From the dawn of time, until SDL 2.0.6, there was only one way to convert audio through SDL: By using the `SDL_AudioCVT` structure.

It's a usable API, for various needs, but it has a few problems:

- It's hard to understand how to use.
- It can't carry any dynamic state; there's no API to "free" a structure, so it can't allocate memory, or do special things for various converters. In 2.0.6, it even commandeers a pointer in the struct it hopes you aren't using, just to give it space for a few more bits of internal state information. This also leads to some other inefficient tapdances to wedge functionality into it.
- The existing structure is extremely rigid, expecting certain fields to be set by the app and certain fields to be set by SDL, and there is no room for expansion. Did I mention we steal a pointer field?
- Perhaps most importantly: **it can't resample data in chunks**. You have to give it all the data it expects in one shot, or you'll get gaps and skips in your audio output.

We have a better API that SDL has been using internally for awhile now, since it needs to bridge data between the app's audio callbacks and the platform APIs that consume and produce data, and that data might be coming and going at any size and format at inexact times. Not only does this API have to convert and resample data on the fly, it needs to be able to buffer it when one end produces data at a different rate than the other is consuming it.

In SDL2, we've cleaned up these internal APIs and made them available to apps. We call it [SDL_AudioStream](SDL_AudioStream). In SDL3, SDL_AudioStream is the backbone of the entire audio subsystem.

Here are some immediate uses for SDL_AudioStream:

- You want to decode an Ogg Vorbis file, and convert it to a specific format for playback on the fly, but libvorbis only hands you 512 bytes of uncompressed data at a time. You can push it through an [[SDL_AudioStream]] a drip at a time, and pull converted data out of the other side, in a different format, as needed.
- You have a VoIP app, but you can't promise when audio packets will arrive over the network, or how large those packets will be when they do, or if you'll have to replace them with a chunk of silence when they don't arrive at all...but you want to be able to produce a single coherent stream of audio data, ready for playback.
- You want to pull audio data from disk as fast as possible, stuff it into something that will do the proper conversions, and dump the results back to disk without having to worry about the details of the data as it's passing through.
- You want to write a mixer that only deals with a single specific format and have it output to whatever else might need to eat that data.
- You have some procedurally-generated sound and want to produce more when most of it has been consumed.
- You have no interest in converting audio to a different format, but you just want someone else to worry about storing it in an efficient, queue-like data structure until you are ready to make use of it.

Using SDL_AudioStream is pretty simple. First, you create one. Let's say you want to produce mono data in Sint16 format at 22050Hz, for something that wants to consume stereo data in Float32 format at 48000Hz.

```c
// You put data at Sint16/mono/22050Hz, you get back data at Float32/stereo/48000Hz.
SDL_AudioStream *stream = SDL_CreateAudioStream(AUDIO_S16, 1, 22050, AUDIO_F32, 2, 48000);
if (stream == NULL) {
    printf("Uhoh, stream failed to create: %s\n", SDL_GetError());
} else {
    // We are ready to use the stream!
}
```

Now all you have to do is feed your stream data!

```c
Sint16 samples[1024];
int num_samples = read_more_samples_from_disk(samples); // whatever.
// you tell it the number of _bytes_, not samples, you're putting!
int rc = SDL_PutAudioStreamData(stream, samples, num_samples * sizeof (Sint16));
if (rc == -1) {
    printf("Uhoh, failed to put samples in stream: %s\n", SDL_GetError());
    return;
}

// Whoops, forgot to add a single sample at the end...!
//  You can put any amount at once, SDL will buffer
//  appropriately, growing the buffer if necessary.
Sint16 onesample = 22;
SDL_PutAudioStreamData(stream, &onesample, sizeof (Sint16));
```

As you add data to the stream, SDL will convert and resample it. You can ask how much converted data is available:

```c
int avail = SDL_GetAudioStreamAvailable(stream);  // this is in bytes, not samples!
if (avail < 100) {
    printf("I'm still waiting on %d bytes of data!\n", 100 - avail);
}
```

And when you have enough data to be useful, you can read out samples in the requested format:

```c
float converted[100];
// this is in bytes, not samples!
int gotten = SDL_GetAudioStreamData(stream, converted, sizeof (converted));
if (gotten == -1) {
    printf("Uhoh, failed to get converted data: %s\n", SDL_GetError());
}
write_more_samples_to_disk(converted, gotten); /* whatever. */
```

Of course, you don't have to read it all at once. This both streams in _and_ out of a converted buffer, so you can read less than is available:

```c
int gotten;
do {
    float converted[100];
    // this is in bytes, not samples!
    gotten = SDL_GetAudioStreamData(stream, converted, sizeof (converted));
    if (gotten == -1) {
        printf("Uhoh, failed to get converted data: %s\n", SDL_GetError());
    } else {
        // (gotten) might be less than requested in SDL_GetAudioStreamData!
        write_more_samples_to_disk(converted, gotten); /* whatever. */
    }
} while (gotten > 0);
```

In terms of performance: buffer allocations, conversion, and resampling happen during stream gets. Putting to the stream is a little bookkeeping and some SDL_memcpy() calls. Plan accordingly.

The one gotcha of this interface: you might notice that you have less available than you expect (possibly even zero bytes available!). When resampling, SDL keeps a buffer of padding available so that data sent through in chunks still resamples smoothly. Rather than try to predict the future, it just holds onto the first little piece you feed into the stream, and then starts converting that part after it's received more data, holding a tiny bit back each time to keep the stream sounding smooth.

There are two ways to deal with this: if you're planning to stream forever, don't do anything. Just keep feeding more data as you have it, and reading more data from the stream as it becomes available, and it'll all work out.

If you are simply at the end of the data you want to stream, you can communicate this to SDL and it will convert any buffered data it's been holding onto internally, making it available to be read with [SDL_GetAudioStreamData](SDL_GetAudioStreamData)().

```c
SDL_FlushAudioStream(stream);
```

Note that if you flush a stream, you can then feed it more data, but there will likely be gaps in the audio output, as the resampler will use silence for the padding at the end. You really only want to flush to finish off a stream and get the last few samples out of it.

If, for whatever reason, you want to throw a stream's contents away without reading it, you can:

```c
SDL_ClearAudioStream(stream);
```

This will remove any data you've put to the stream without reading, and reset internal state (so the resampler will be expecting a fresh buffer instead of resampling against data you previously wrote to the stream). This is useful if you plan to reuse a stream for different source, or just decided that the current source wasn't working out; maybe you're muting an offensive person on a VoIP app.

When you are done with the stream, you can destroy it:

```c
SDL_DestroyAudioStream(stream);
```

This frees up internal state and buffers. You don't have to drain the stream before freeing it. The SDL_AudioStream pointer you've been using is invalid after this call.

That's all!
