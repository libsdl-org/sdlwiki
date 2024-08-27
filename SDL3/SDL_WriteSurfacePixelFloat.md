###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteSurfacePixelFloat

Writes a single pixel to a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_WriteSurfacePixelFloat(SDL_Surface *surface, int x, int y, float r, float g, float b, float a);
```

## Function Parameters

|                              |             |                                                     |
| ---------------------------- | ----------- | --------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to write.                               |
| int                          | **x**       | the horizontal coordinate, 0 <= x < width.          |
| int                          | **y**       | the vertical coordinate, 0 <= y < height.           |
| float                        | **r**       | the red channel value, normally in the range 0-1.   |
| float                        | **g**       | the green channel value, normally in the range 0-1. |
| float                        | **b**       | the blue channel value, normally in the range 0-1.  |
| float                        | **a**       | the alpha channel value, normally in the range 0-1. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This function prioritizes correctness over speed: it is suitable for unit
tests, but is not intended for use in a game engine.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

