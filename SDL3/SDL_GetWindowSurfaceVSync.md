###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowSurfaceVSync

Get VSync for the window surface.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_GetWindowSurfaceVSync(SDL_Window *window, int *vsync);
```

## Function Parameters

|                            |            |                                                                                                                                                           |
| -------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query.                                                                                                                                      |
| int *                      | **vsync**  | an int filled with the current vertical refresh sync interval. See [SDL_SetWindowSurfaceVSync](SDL_SetWindowSurfaceVSync)() for the meaning of the value. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowSurfaceVSync](SDL_SetWindowSurfaceVSync)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

