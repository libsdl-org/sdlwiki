###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetRenderVSync

Toggle VSync of the given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderVSync(SDL_Renderer *renderer, int vsync);


#define SDL_RENDERER_VSYNC_DISABLED 0
#define SDL_RENDERER_VSYNC_ADAPTIVE (-1)
```

## Function Parameters

|                                |              |                                     |
| ------------------------------ | ------------ | ----------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer to toggle.             |
| int                            | **vsync**    | the vertical refresh sync interval. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When a renderer is created, vsync defaults to
[SDL_RENDERER_VSYNC_DISABLED](SDL_RENDERER_VSYNC_DISABLED).

The `vsync` parameter can be 1 to synchronize present with every vertical
refresh, 2 to synchronize present with every second vertical refresh, etc.,
[SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE](SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE) for
late swap tearing (adaptive vsync), or
[SDL_WINDOW_SURFACE_VSYNC_DISABLED](SDL_WINDOW_SURFACE_VSYNC_DISABLED) to
disable. Not every value is supported by every driver, so you should check
the return value to see whether the requested setting is supported.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderVSync](SDL_GetRenderVSync)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

