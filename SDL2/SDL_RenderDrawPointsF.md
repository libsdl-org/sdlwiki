###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawPointsF

Draw multiple points on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderDrawPointsF(SDL_Renderer * renderer,
                          const SDL_FPoint * points,
                          int count);

```

## Function Parameters

|                  |                                                 |
| ---------------- | ----------------------------------------------- |
| **renderer**     | The renderer which should draw multiple points. |
| **points**       | The points to draw                              |
| **count**        | The number of points to draw                    |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI)

