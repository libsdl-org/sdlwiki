###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowMaximumSize

Get the maximum size of a window's client area.

## Syntax

```c
void SDL_GetWindowMaximumSize(SDL_Window * window,
                              int *w, int *h);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **window**     | the window to query                                                    |
| **w**          | a pointer filled in with the maximum width of the window, may be NULL  |
| **h**          | a pointer filled in with the maximum height of the window, may be NULL |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowMinimumSize](SDL_GetWindowMinimumSize.md)
* [SDL_SetWindowMaximumSize](SDL_SetWindowMaximumSize.md)

----
[CategoryAPI](CategoryAPI.md)
