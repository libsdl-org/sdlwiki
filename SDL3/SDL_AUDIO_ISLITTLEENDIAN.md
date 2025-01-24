# SDL_AUDIO_ISLITTLEENDIAN

Determine if an [SDL_AudioFormat](SDL_AudioFormat) represents littleendian data.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_AUDIO_ISLITTLEENDIAN(x)  (!SDL_AUDIO_ISBIGENDIAN(x))
```

## Macro Parameters

|       |                                              |
| ----- | -------------------------------------------- |
| **x** | an [SDL_AudioFormat](SDL_AudioFormat) value. |

## Return Value

Returns non-zero if format is littleendian, zero otherwise.

## Remarks

For example, `SDL_AUDIO_ISLITTLEENDIAN(SDL_AUDIO_S16BE)` returns 0.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

