# SDL_ReadSurfacePixel

Retrieves a single pixel from a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_ReadSurfacePixel(SDL_Surface *surface, int x, int y, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
```

## Function Parameters

|                              |             |                                                                                    |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to read.                                                               |
| int                          | **x**       | the horizontal coordinate, 0 <= x < width.                                         |
| int                          | **y**       | the vertical coordinate, 0 <= y < height.                                          |
| Uint8 *                      | **r**       | a pointer filled in with the red channel, 0-255, or NULL to ignore this channel.   |
| Uint8 *                      | **g**       | a pointer filled in with the green channel, 0-255, or NULL to ignore this channel. |
| Uint8 *                      | **b**       | a pointer filled in with the blue channel, 0-255, or NULL to ignore this channel.  |
| Uint8 *                      | **a**       | a pointer filled in with the alpha channel, 0-255, or NULL to ignore this channel. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function prioritizes correctness over speed: it is suitable for unit
tests, but is not intended for use in a game engine.

Like [SDL_GetRGBA](SDL_GetRGBA), this uses the entire 0..255 range when
converting color components from pixel formats with less than 8 bits per
RGB component.

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

