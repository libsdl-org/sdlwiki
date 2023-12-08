###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderFillRectF

Fill a rectangle on the current rendering target with the drawing color at subpixel precision.

## Syntax

```c
int SDL_RenderFillRectF(SDL_Renderer * renderer,
                        const SDL_FRect * rect);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should fill a rectangle.                                      |
| **rect**         | A pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI.md)
