# SDL_SetRenderScale

Set the drawing scale for rendering on the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderScale(SDL_Renderer *renderer, float scaleX, float scaleY);
```

## Function Parameters

|                                |              |                                |
| ------------------------------ | ------------ | ------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.         |
| float                          | **scaleX**   | the horizontal scaling factor. |
| float                          | **scaleY**   | the vertical scaling factor.   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The drawing coordinates are scaled by the x/y scaling factors before they
are used by the renderer. This allows resolution independent drawing with a
single coordinate system.

If this results in scaling or subpixel drawing by the rendering backend, it
will be handled using the appropriate quality hints. For best results use
integer scaling factors.

Each render target has its own scale. This function sets the scale for the
current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderScale](SDL_GetRenderScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

