# SDL_GetRenderClipRect

Get the clip rectangle for the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetRenderClipRect(SDL_Renderer *renderer, SDL_Rect *rect);
```

## Function Parameters

|                                |              |                                                                                                                           |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                    |
| [SDL_Rect](SDL_Rect) *         | **rect**     | an [SDL_Rect](SDL_Rect) structure filled in with the current clipping area or an empty rectangle if clipping is disabled. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each render target has its own clip rectangle. This function gets the
cliprect for the current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderClipEnabled](SDL_RenderClipEnabled)
- [SDL_SetRenderClipRect](SDL_SetRenderClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

