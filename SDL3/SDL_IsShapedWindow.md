###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsShapedWindow

Return whether the given window is a shaped window.

## Syntax

```c
SDL_bool SDL_IsShapedWindow(const SDL_Window *window);

```

## Function Parameters

|                |                                       |
| -------------- | ------------------------------------- |
| **window**     | The window to query for being shaped. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the window is a window that can be shaped,
[SDL_FALSE](SDL_FALSE) if the window is unshaped or NULL.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateShapedWindow](SDL_CreateShapedWindow)

----
[CategoryAPI](CategoryAPI)

