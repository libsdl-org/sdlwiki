###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowPosition

Get the position of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_GetWindowPosition(SDL_Window * window,
                           int *x, int *y);

```

## Function Parameters

|                |                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------- |
| **window**     | the window to query                                                                       |
| **x**          | a pointer filled in with the x position of the window, in screen coordinates, may be NULL |
| **y**          | a pointer filled in with the y position of the window, in screen coordinates, may be NULL |

## Remarks

If you do not need the value for one of the positions a NULL may be passed
in the `x` or `y` parameter.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetWindowPosition](SDL_SetWindowPosition)

----
[CategoryAPI](CategoryAPI)

