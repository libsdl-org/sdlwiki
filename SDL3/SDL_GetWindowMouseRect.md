###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowMouseRect

Get the mouse confinement rectangle of a window.

## Syntax

```c
const SDL_Rect* SDL_GetWindowMouseRect(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | The window to query |

## Return Value

Returns A pointer to the mouse confinement rectangle of a window, or NULL
if there isn't one.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowMouseRect](SDL_SetWindowMouseRect)

----
[CategoryAPI](CategoryAPI)

