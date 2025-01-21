###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AUDIO_MASK_BIG_ENDIAN

Mask of bits in an [SDL_AudioFormat](SDL_AudioFormat) that contain the bigendian flag.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_AUDIO_MASK_BIG_ENDIAN    (1u<<12)
```

## Remarks

Generally one should use [SDL_AUDIO_ISBIGENDIAN](SDL_AUDIO_ISBIGENDIAN) or
[SDL_AUDIO_ISLITTLEENDIAN](SDL_AUDIO_ISLITTLEENDIAN) instead of this macro
directly.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

