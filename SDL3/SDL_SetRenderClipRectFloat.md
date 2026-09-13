# SDL_SetRenderClipRectFloat

Set the clip rectangle for rendering on the specified target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderClipRectFloat(SDL_Renderer *renderer, const SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                                                                        |
| ------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                 |
| const [SDL_FRect](SDL_FRect) * | **rect**     | an [SDL_FRect](SDL_FRect) structure representing the clip area, relative to the viewport, or NULL to disable clipping. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each render target has its own clip rectangle. This function sets the
cliprect for the current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetRenderClipRectFloat](SDL_GetRenderClipRectFloat)
- [SDL_RenderClipEnabled](SDL_RenderClipEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

