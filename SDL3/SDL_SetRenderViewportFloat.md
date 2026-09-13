# SDL_SetRenderViewportFloat

Set the drawing area for rendering on the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderViewportFloat(SDL_Renderer *renderer, const SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                                                                       |
| ------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                |
| const [SDL_FRect](SDL_FRect) * | **rect**     | the [SDL_FRect](SDL_FRect) structure representing the drawing area, or NULL to set the viewport to the entire target. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Drawing will clip to this area (separately from any clipping done with
[SDL_SetRenderClipRect](SDL_SetRenderClipRect)), and the top left of the
area will become coordinate (0, 0) for future drawing commands.

The area's width and height must be >= 0.

Each render target has its own viewport. This function sets the viewport
for the current render target.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetRenderViewportFloat](SDL_GetRenderViewportFloat)
- [SDL_RenderViewportSet](SDL_RenderViewportSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

