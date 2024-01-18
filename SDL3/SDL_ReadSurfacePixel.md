###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadSurfacePixel

Retrieves a single pixel from a surface.

## Syntax

```c
int SDL_ReadSurfacePixel(SDL_Surface *surface, int x, int y, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);

```

## Function Parameters

|                 |                                                                                   |
| --------------- | --------------------------------------------------------------------------------- |
| **surface**     | the surface to read                                                               |
| **x**           | the horizontal coordinate, 0 <= x < width                                         |
| **y**           | the vertical coordinate, 0 <= y < height                                          |
| **r**           | a pointer filled in with the red channel, 0-255, or NULL to ignore this channel   |
| **g**           | a pointer filled in with the green channel, 0-255, or NULL to ignore this channel |
| **b**           | a pointer filled in with the blue channel, 0-255, or NULL to ignore this channel  |
| **a**           | a pointer filled in with the alpha channel, 0-255, or NULL to ignore this channel |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function prioritizes correctness over speed: it is suitable for unit
tests, but is not intended for use in a game engine.

Like [SDL_GetRGBA](SDL_GetRGBA), this uses the entire 0..255 range when
converting color components from pixel formats with less than 8 bits per
RGB component.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

