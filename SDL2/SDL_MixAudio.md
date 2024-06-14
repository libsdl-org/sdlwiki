###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MixAudio

This function is a legacy means of mixing audio.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_MixAudio(Uint8 * dst, const Uint8 * src,
              Uint32 len, int volume);
```

## Function Parameters

|               |            |                                                                                                         |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------- |
| Uint8 *       | **dst**    | the destination for the mixed audio.                                                                    |
| const Uint8 * | **src**    | the source audio buffer to be mixed.                                                                    |
| Uint32        | **len**    | the length of the audio buffer in bytes.                                                                |
| int           | **volume** | ranges from 0 - 128, and should be set to [SDL_MIX_MAXVOLUME](SDL_MIX_MAXVOLUME) for full audio volume. |

## Remarks

This function is equivalent to calling...

```c
SDL_MixAudioFormat(dst, src, format, len, volume);
```

...where `format` is the obtained format of the audio device from the
legacy [SDL_OpenAudio](SDL_OpenAudio)() function.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_MixAudioFormat](SDL_MixAudioFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

