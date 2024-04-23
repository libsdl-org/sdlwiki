###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MixAudioFormat

Mix audio data in a specified format.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_MixAudioFormat(Uint8 * dst,
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

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

