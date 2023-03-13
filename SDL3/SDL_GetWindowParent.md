###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowParent

Get parent of a window.

## Syntax

```c
SDL_Window* SDL_GetWindowParent(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the parent of the window on success or NULL if the window has no
parent.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePopupWindow](SDL_CreatePopupWindow)

----
[CategoryAPI](CategoryAPI)

