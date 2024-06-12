###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderLogicalToWindow

Get real coordinates of point in window when given logical coordinates of point in renderer.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
void SDL_RenderLogicalToWindow(SDL_Renderer * renderer, 
                                float logicalX, float logicalY,
                                int *windowX, int *windowY);
```

## Function Parameters

|                                |              |                                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer from which the window coordinates should be calculated |
| float                          | **logicalX** | the logical x coordinate                                            |
| float                          | **logicalY** | the logical y coordinate                                            |
| int *                          | **windowX**  | the pointer filled with the real X coordinate in the window         |
| int *                          | **windowY**  | the pointer filled with the real Y coordinate in the window         |

## Remarks

Logical coordinates will differ from real coordinates when render is scaled
and logical renderer size set

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_RenderGetScale](SDL_RenderGetScale)
- [SDL_RenderSetScale](SDL_RenderSetScale)
- [SDL_RenderGetLogicalSize](SDL_RenderGetLogicalSize)
- [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

