###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AUDIO_FRAMESIZE

Calculate the size of each audio frame (in bytes) from an [SDL_AudioSpec](SDL_AudioSpec).

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_AUDIO_FRAMESIZE(x) (SDL_AUDIO_BYTESIZE((x).format) * (x).channels)
```

## Macro Parameters

|       |                                             |
| ----- | ------------------------------------------- |
| **x** | an [SDL_AudioSpec](SDL_AudioSpec) to query. |

## Return Value

Returns the number of bytes used per sample frame.

## Remarks

This reports on the size of an audio sample frame: stereo Sint16 data (2
channels of 2 bytes each) would be 4 bytes per frame, for example.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

