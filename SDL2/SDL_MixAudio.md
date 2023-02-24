###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MixAudio

This function is a legacy means of mixing audio.

## Syntax

```c
void SDL_MixAudio(Uint8 * dst, const Uint8 * src,
                  Uint32 len, int volume);

```

## Function Parameters

|                |                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| **dst**        | the destination for the mixed audio                                                                    |
| **src**        | the source audio buffer to be mixed                                                                    |
| **len**        | the length of the audio buffer in bytes                                                                |
| **volume**     | ranges from 0 - 128, and should be set to [SDL_MIX_MAXVOLUME](SDL_MIX_MAXVOLUME) for full audio volume |

## Remarks

This function is equivalent to calling...

```c
SDL_MixAudioFormat(dst, src, format, len, volume);
```

...where `format` is the obtained format of the audio device from the
legacy [SDL_OpenAudio](SDL_OpenAudio)() function.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_MixAudioFormat](SDL_MixAudioFormat)

----
[CategoryAPI](CategoryAPI)

