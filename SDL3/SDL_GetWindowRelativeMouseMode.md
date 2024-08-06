###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowRelativeMouseMode

Query whether relative mouse mode is enabled for a window.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_bool SDL_GetWindowRelativeMouseMode(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if relative mode is
enabled for a window or [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowRelativeMouseMode](SDL_SetWindowRelativeMouseMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

