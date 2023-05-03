###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_OpenAudio

Open the default audio device for playback.

## Syntax

```c
int Mix_OpenAudio(int frequency, Uint16 format, int channels, int chunksize);

```

## Function Parameters

|                   |                                                                              |
| ----------------- | ---------------------------------------------------------------------------- |
| **frequency**     | the frequency to playback audio at (in Hz).                                  |
| **format**        | audio format, one of SDL's SDL_AUDIO_* values.                               |
| **channels**      | number of channels (1 is mono, 2 is stereo, etc).                            |
| **chunksize**     | audio buffer size in sample FRAMES (total samples divided by channel count). |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

An audio device is what generates sound, so the app must open one to make
noise.

This function will check if SDL's audio system is initialized, and if not,
it will initialize it by calling `SDL_Init(SDL_INIT_AUDIO)` on your behalf.
You are free to (and encouraged to!) initialize it yourself before calling
this function, as this gives your program more control over the process.

This function might cover all of an application's needs, but for those that
need more flexibility, the more powerful version of this function is
[Mix_OpenAudioDevice](Mix_OpenAudioDevice)(). This function is equivalent
to calling:

```c
Mix_OpenAudioDevice(frequency, format, nchannels, chunksize, NULL,
                    SDL_AUDIO_ALLOW_FREQUENCY_CHANGE |
                    SDL_AUDIO_ALLOW_CHANNELS_CHANGE);
```

If you aren't particularly concerned with the specifics of the audio
device, and your data isn't in a specific format, the values you use here
can just be reasonable defaults. SDL_mixer will convert audio data you feed
it to the correct format on demand.

That being said, if you have control of your audio data and you know its
format ahead of time, you can save CPU time by opening the audio device in
that exact format so SDL_mixer does not have to spend time converting
anything behind the scenes, and can just pass the data straight through to
the hardware. On some platforms, where the hardware only supports specific
settings, you might have to be careful to make everything match, but your
own data is often easier to control, so aim to open the device for what you
need.

The other reason to care about specific formats: if you plan to touch the
mix buffer directly (with [Mix_SetPostMix](Mix_SetPostMix), a registered
effect, or [Mix_HookMusic](Mix_HookMusic)), you might have code that
expects it to be in a specific format, and you should specify that here.

The audio device frequency is specified in Hz; in modern times, 48000 is
often a reasonable default.

The audio device format is one of SDL's SDL_AUDIO_* constants.
SDL_AUDIO_S16SYS (16-bit audio) is probably a safe default. More modern
systems may prefer SDL_AUDIO_F32SYS (32-bit floating point audio).

The audio device channels are generally 1 for mono output, or 2 for stereo,
but the brave can try surround sound configs with 4 (quad), 6 (5.1), 7
(6.1) or 8 (7.1).

The audio device's chunk size is the number of sample frames (one sample
per frame for mono output, two samples per frame in a stereo setup, etc)
that are fed to the device at once. The lower the number, the lower the
latency, but you risk dropouts if it gets too low. 2048 is often a
reasonable default, but your app might want to experiment with 1024 or
4096.

You may only have one audio device open at a time; if you want to change a
setting, you must close the device and reopen it, which is not something
you can do seamlessly during playback.

This function does not allow you to select a specific audio device on the
system, it always chooses the best default it can on your behalf (which, in
many cases, is exactly what you want anyhow). If you must choose a specific
device, you can do so with [Mix_OpenAudioDevice](Mix_OpenAudioDevice)()
instead.

If this function reports success, you are ready to start making noise! Load
some audio data and start playing!

The app can use [Mix_QuerySpec](Mix_QuerySpec)() to determine the final
device settings.

When done with an audio device, probably at the end of the program, the app
should dispose of the device with [Mix_CloseAudio](Mix_CloseAudio)().

## Version

This function is available since SDL_mixer 2.0.0.

## Related Functions

* [Mix_OpenAudioDevice](Mix_OpenAudioDevice)
* [Mix_CloseAudio](Mix_CloseAudio)

----
[CategoryAPI](CategoryAPI)

