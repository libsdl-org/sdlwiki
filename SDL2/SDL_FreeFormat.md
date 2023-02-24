###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeFormat

Free an [SDL_PixelFormat](SDL_PixelFormat) structure allocated by [SDL_AllocFormat](SDL_AllocFormat)().

## Syntax

```c
void SDL_FreeFormat(SDL_PixelFormat *format);

```

## Function Parameters

|                |                                                          |
| -------------- | -------------------------------------------------------- |
| **format**     | the [SDL_PixelFormat](SDL_PixelFormat) structure to free |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AllocFormat](SDL_AllocFormat)

----
[CategoryAPI](CategoryAPI)

