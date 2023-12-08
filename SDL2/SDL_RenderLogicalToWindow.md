###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderLogicalToWindow

Get real coordinates of point in window when given logical coordinates of point in renderer.

## Syntax

```c
void SDL_RenderLogicalToWindow(SDL_Renderer * renderer,
                                    float logicalX, float logicalY,
                                    int *windowX, int *windowY);

```

## Function Parameters

|                  |                                                                     |
| ---------------- | ------------------------------------------------------------------- |
| **renderer**     | the renderer from which the window coordinates should be calculated |
| **logicalX**     | the logical x coordinate                                            |
| **logicalY**     | the logical y coordinate                                            |
| **windowX**      | the pointer filled with the real X coordinate in the window         |
| **windowY**      | the pointer filled with the real Y coordinate in the window         |

## Remarks

Logical coordinates will differ from real coordinates when render is scaled
and logical renderer size set

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_RenderGetScale](SDL_RenderGetScale.md)
* [SDL_RenderSetScale](SDL_RenderSetScale.md)
* [SDL_RenderGetLogicalSize](SDL_RenderGetLogicalSize.md)
* [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize.md)

----
[CategoryAPI](CategoryAPI.md)
