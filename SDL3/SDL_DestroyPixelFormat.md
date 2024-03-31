###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyPixelFormat

Free an [SDL_PixelFormat](SDL_PixelFormat) structure allocated by [SDL_CreatePixelFormat](SDL_CreatePixelFormat)().

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_DestroyPixelFormat(SDL_PixelFormat *format);

```

## Function Parameters

|                |                                                          |
| -------------- | -------------------------------------------------------- |
| **format**     | the [SDL_PixelFormat](SDL_PixelFormat) structure to free |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePixelFormat](SDL_CreatePixelFormat)

----
[CategoryAPI](CategoryAPI)

