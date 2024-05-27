###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowSurfaceVSync

Toggle VSync for the window surface.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowSurfaceVSync(SDL_Window *window, int vsync);


#define SDL_WINDOW_SURFACE_VSYNC_DISABLED 0
#define SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE (-1)
```

## Function Parameters

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **vsync**      | the vertical refresh sync interval, 1 to synchronize present with every vertical refresh, 2 to synchronize present with every second vertical refresh, etc., [SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE](SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE) for late swap tearing (adaptive vsync), or [SDL_WINDOW_SURFACE_VSYNC_DISABLED](SDL_WINDOW_SURFACE_VSYNC_DISABLED) to disable. Not every value is supported by every driver, so you should check the return value to see whether the requested setting is supported. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When a window surface is created, vsync defaults to
[SDL_WINDOW_SURFACE_VSYNC_DISABLED](SDL_WINDOW_SURFACE_VSYNC_DISABLED).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowSurfaceVSync](SDL_GetWindowSurfaceVSync)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

