# SDL_IsShapedWindow

Return whether the given window is a shaped window.

## Header File

Defined in [SDL_shape.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_shape.h)

## Syntax

```c
SDL_bool SDL_IsShapedWindow(const SDL_Window *window);
```

## Function Parameters

|                                  |            |                                       |
| -------------------------------- | ---------- | ------------------------------------- |
| const [SDL_Window](SDL_Window) * | **window** | The window to query for being shaped. |

## Return Value

([SDL_bool](SDL_bool)) Return [SDL_TRUE](SDL_TRUE) if the window is a
window that can be shaped, [SDL_FALSE](SDL_FALSE) if the window is unshaped
or NULL.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateShapedWindow](SDL_CreateShapedWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryShape](CategoryShape)

