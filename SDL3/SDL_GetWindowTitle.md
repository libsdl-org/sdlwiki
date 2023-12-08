###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowTitle

Get the title of a window.

## Syntax

```c
const char* SDL_GetWindowTitle(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the title of the window in UTF-8 format or "" if there is no title.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowTitle](SDL_SetWindowTitle.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
