# SDL_RenderClipEnabled

Get whether clipping is enabled on the given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderClipEnabled(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Return Value

(bool) Returns true if clipping is enabled or false if not; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderClipRect](SDL_GetRenderClipRect)
- [SDL_SetRenderClipRect](SDL_SetRenderClipRect)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

