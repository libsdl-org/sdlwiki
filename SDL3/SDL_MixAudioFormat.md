###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MixAudioFormat

Mix audio data in a specified format.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_MixAudioFormat(Uint8 * dst,
                       const Uint8 * src,
                       SDL_AudioFormat format,
                       Uint32 len, int volume);

```

## Function Parameters

|                |                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| **dst**        | the destination for the mixed audio                                                                    |
| **src**        | the source audio buffer to be mixed                                                                    |
| **format**     | the [SDL_AudioFormat](SDL_AudioFormat) structure representing the desired audio format                 |
| **len**        | the length of the audio buffer in bytes                                                                |
| **volume**     | ranges from 0 - 128, and should be set to [SDL_MIX_MAXVOLUME](SDL_MIX_MAXVOLUME) for full audio volume |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This takes an audio buffer `src` of `len` bytes of `format` data and mixes
it into `dst`, performing addition, volume adjustment, and overflow
clipping. The buffer pointed to by `dst` must also be `len` bytes of
`format` data.

This is provided for convenience -- you can mix your own audio data.

Do not use this function for mixing together more than two streams of
sample data. The output from repeated application of this function may be
distorted by clipping, because there is no accumulator with greater range
than the input (not to mention this being an inefficient way of doing it).

It is a common misconception that this function is required to write audio
data to an output stream in an audio callback. While you can do that,
[SDL_MixAudioFormat](SDL_MixAudioFormat)() is really only needed when
you're mixing a single audio stream with a volume adjustment.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c

void MyAudioCallback(void *udata, Uint8 *stream, int len)
{
    extern SDL_AudioFormat deviceFormat;
    extern const Uint8 *mixData;
    SDL_memset(stream, 0, len);  // make sure this is silence.
    // mix our audio against the silence, at 50% volume.
    SDL_MixAudioFormat(stream, mixData, deviceFormat, len, SDL_MIX_MAXVOLUME / 2);
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)


