###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowPosition

Get the position of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetWindowPosition(SDL_Window *window, int *x, int *y);

```

## Function Parameters

|                |                                                                    |
| -------------- | ------------------------------------------------------------------ |
| **window**     | the window to query                                                |
| **x**          | a pointer filled in with the x position of the window, may be NULL |
| **y**          | a pointer filled in with the y position of the window, may be NULL |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is the current position of the window as last reported by the
windowing system.

If you do not need the value for one of the positions a NULL may be passed
in the `x` or `y` parameter.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowPosition](SDL_SetWindowPosition)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


