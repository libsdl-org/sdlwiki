# SDL_ReadSurfacePixelFloat

Retrieves a single pixel from a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_ReadSurfacePixelFloat(SDL_Surface *surface, int x, int y, float *r, float *g, float *b, float *a);
```

## Function Parameters

|                              |             |                                                                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to read.                                                                                   |
| int                          | **x**       | the horizontal coordinate, 0 <= x < width.                                                             |
| int                          | **y**       | the vertical coordinate, 0 <= y < height.                                                              |
| float *                      | **r**       | a pointer filled in with the red channel, normally in the range 0-1, or NULL to ignore this channel.   |
| float *                      | **g**       | a pointer filled in with the green channel, normally in the range 0-1, or NULL to ignore this channel. |
| float *                      | **b**       | a pointer filled in with the blue channel, normally in the range 0-1, or NULL to ignore this channel.  |
| float *                      | **a**       | a pointer filled in with the alpha channel, normally in the range 0-1, or NULL to ignore this channel. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function prioritizes correctness over speed: it is suitable for unit
tests, but is not intended for use in a game engine.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

