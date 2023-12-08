###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderWindowToLogical

Get logical coordinates of point in renderer when given real coordinates of point in window.

## Syntax

```c
void SDL_RenderWindowToLogical(SDL_Renderer * renderer,
                                    int windowX, int windowY,
                                    float *logicalX, float *logicalY);

```

## Function Parameters

|                  |                                                                      |
| ---------------- | -------------------------------------------------------------------- |
| **renderer**     | the renderer from which the logical coordinates should be calculated |
| **windowX**      | the real X coordinate in the window                                  |
| **windowY**      | the real Y coordinate in the window                                  |
| **logicalX**     | the pointer filled with the logical x coordinate                     |
| **logicalY**     | the pointer filled with the logical y coordinate                     |

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
