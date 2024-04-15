###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Color

A structure that represents a color as RGBA components.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_Color
{
    Uint8 r;
    Uint8 g;
    Uint8 b;
    Uint8 a;
} SDL_Color;
```

## Remarks

The bits of this structure can be directly reinterpreted as an
integer-packed color which uses the
[SDL_PIXELFORMAT_RGBA32](SDL_PIXELFORMAT_RGBA32) format
([SDL_PIXELFORMAT_ABGR8888](SDL_PIXELFORMAT_ABGR8888) on little-endian
systems and [SDL_PIXELFORMAT_RGBA8888](SDL_PIXELFORMAT_RGBA8888) on
big-endian systems).

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

