###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderSetScale

Set the drawing scale for rendering on the current target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderSetScale(SDL_Renderer * renderer,
                   float scaleX, float scaleY);
```

## Function Parameters

|                                |              |                                |
| ------------------------------ | ------------ | ------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | a rendering context.           |
| float                          | **scaleX**   | the horizontal scaling factor. |
| float                          | **scaleY**   | the vertical scaling factor.   |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The drawing coordinates are scaled by the x/y scaling factors before they
are used by the renderer. This allows resolution independent drawing with a
single coordinate system.

If this results in scaling or subpixel drawing by the rendering backend, it
will be handled using the appropriate quality hints. For best results use
integer scaling factors.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RenderGetScale](SDL_RenderGetScale)
- [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

