###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AUDIO_BYTESIZE

Retrieve the size, in bytes, from an [SDL_AudioFormat](SDL_AudioFormat).

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_AUDIO_BYTESIZE(x)        (SDL_AUDIO_BITSIZE(x) / 8)
```

## Macro Parameters

|       |                                             |
| ----- | ------------------------------------------- |
| **x** | an [SDL_AudioFormat](SDL_AudioFormat) value |

## Return Value

Returns data size in bytes

## Remarks

For example, `SDL_AUDIO_BYTESIZE(SDL_AUDIO_S16)` returns 2.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

