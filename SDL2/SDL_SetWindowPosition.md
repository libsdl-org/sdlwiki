###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowPosition

Set the position of a window.

## Syntax

```c
void SDL_SetWindowPosition(SDL_Window * window,
                           int x, int y);

```

## Function Parameters

|                |                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window to reposition                                                                                                                                            |
| **x**          | the x coordinate of the window in screen coordinates, or `[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED)` or `[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED)` |
| **y**          | the y coordinate of the window in screen coordinates, or `[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED)` or `[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED)` |

## Remarks

The window coordinate origin is the upper left of the display.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowPosition](SDL_GetWindowPosition)

----
[CategoryAPI](CategoryAPI)

