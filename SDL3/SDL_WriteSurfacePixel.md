###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteSurfacePixel

Writes a single pixel to a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_WriteSurfacePixel(SDL_Surface *surface, int x, int y, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
```

## Function Parameters

|                              |             |                                            |
| ---------------------------- | ----------- | ------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to write.                      |
| int                          | **x**       | the horizontal coordinate, 0 <= x < width. |
| int                          | **y**       | the vertical coordinate, 0 <= y < height.  |
| Uint8                        | **r**       | the red channel value, 0-255.              |
| Uint8                        | **g**       | the green channel value, 0-255.            |
| Uint8                        | **b**       | the blue channel value, 0-255.             |
| Uint8                        | **a**       | the alpha channel value, 0-255.            |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This function prioritizes correctness over speed: it is suitable for unit
tests, but is not intended for use in a game engine.

Like [SDL_MapRGBA](SDL_MapRGBA), this uses the entire 0..255 range when
converting color components from pixel formats with less than 8 bits per
RGB component.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

