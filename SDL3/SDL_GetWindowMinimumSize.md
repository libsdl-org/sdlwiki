###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowMinimumSize

Get the minimum size of a window's client area.

## Syntax

```c
int SDL_GetWindowMinimumSize(SDL_Window *window, int *w, int *h);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **window**     | the window to query                                                    |
| **w**          | a pointer filled in with the minimum width of the window, may be NULL  |
| **h**          | a pointer filled in with the minimum height of the window, may be NULL |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
* [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)
<!-- #See the Style Guide for instructions on editing the footer. -->


