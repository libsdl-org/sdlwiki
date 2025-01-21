###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WINDOWPOS_UNDEFINED_MASK

A magic value used with [SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED).

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_WINDOWPOS_UNDEFINED_MASK    0x1FFF0000u
```

## Remarks

Generally this macro isn't used directly, but rather through
[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED) or
[SDL_WINDOWPOS_UNDEFINED_DISPLAY](SDL_WINDOWPOS_UNDEFINED_DISPLAY).

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

