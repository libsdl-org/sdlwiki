###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowMinimumSize

Get the minimum size of a window's client area.

## Syntax

```c
void SDL_GetWindowMinimumSize(SDL_Window * window,
                              int *w, int *h);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **window**     | the window to query                                                    |
| **w**          | a pointer filled in with the minimum width of the window, may be NULL  |
| **h**          | a pointer filled in with the minimum height of the window, may be NULL |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize.md)
* [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize.md)

----
[CategoryAPI](CategoryAPI.md)
