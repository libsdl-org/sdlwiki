###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawRectF

Draw a rectangle on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderDrawRectF(SDL_Renderer * renderer,
                        const SDL_FRect * rect);

```

## Function Parameters

|                  |                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should draw a rectangle.                                             |
| **rect**         | A pointer to the destination rectangle, or NULL to outline the entire rendering target. |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI)

