###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowMaximumSize

Set the maximum size of a window's client area.

## Syntax

```c
int SDL_SetWindowMaximumSize(SDL_Window *window, int max_w, int max_h);

```

## Function Parameters

|                |                                                     |
| -------------- | --------------------------------------------------- |
| **window**     | the window to change                                |
| **max_w**      | the maximum width of the window, or 0 for no limit  |
| **max_h**      | the maximum height of the window, or 0 for no limit |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize.md)
* [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
