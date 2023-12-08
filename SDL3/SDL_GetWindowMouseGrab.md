###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowMouseGrab

Get a window's mouse grab mode.

## Syntax

```c
SDL_bool SDL_GetWindowMouseGrab(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if mouse is grabbed, and
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab.md)
* [SDL_GetWindowGrab](SDL_GetWindowGrab.md)

----
[CategoryAPI](CategoryAPI.md)
