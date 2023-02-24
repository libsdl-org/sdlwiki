###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowMinimumSize

Set the minimum size of a window's client area, in screen coordinates.

## Syntax

```c
int SDL_SetWindowMinimumSize(SDL_Window *window, int min_w, int min_h);

```

## Function Parameters

|                |                                  |
| -------------- | -------------------------------- |
| **window**     | the window to change             |
| **min_w**      | the minimum width of the window  |
| **min_h**      | the minimum height of the window |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowMinimumSize](SDL_GetWindowMinimumSize)
* [SDL_SetWindowMaximumSize](SDL_SetWindowMaximumSize)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)
<!-- #See the Style Guide for instructions on editing the footer. -->


