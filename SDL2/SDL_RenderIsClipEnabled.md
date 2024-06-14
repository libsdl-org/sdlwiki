###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderIsClipEnabled

Get whether clipping is enabled on the given renderer.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
SDL_bool SDL_RenderIsClipEnabled(SDL_Renderer * renderer);
```

## Function Parameters

|                                |              |                                                       |
| ------------------------------ | ------------ | ----------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer from which clip state should be queried. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if clipping is enabled
or [SDL_FALSE](SDL_FALSE) if not; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 2.0.4.

## See Also

- [SDL_RenderGetClipRect](SDL_RenderGetClipRect)
- [SDL_RenderSetClipRect](SDL_RenderSetClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

