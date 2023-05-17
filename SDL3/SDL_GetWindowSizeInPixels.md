###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowSizeInPixels

Get the size of a window's client area, in pixels.

## Syntax

```c
int SDL_GetWindowSizeInPixels(SDL_Window *window, int *w, int *h);

```

## Function Parameters

|                |                                                                     |
| -------------- | ------------------------------------------------------------------- |
| **window**     | the window from which the drawable size should be queried           |
| **w**          | a pointer to variable for storing the width in pixels, may be NULL  |
| **h**          | a pointer to variable for storing the height in pixels, may be NULL |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_GetWindowSize](SDL_GetWindowSize)

----
[CategoryAPI](CategoryAPI)

