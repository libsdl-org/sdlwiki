###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawPointF

Draw a point on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderDrawPointF(SDL_Renderer * renderer,
                         float x, float y);

```

## Function Parameters

|                  |                                         |
| ---------------- | --------------------------------------- |
| **renderer**     | The renderer which should draw a point. |
| **x**            | The x coordinate of the point.          |
| **y**            | The y coordinate of the point.          |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI.md)
