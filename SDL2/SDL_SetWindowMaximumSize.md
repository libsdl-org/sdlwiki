###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowMaximumSize

Set the maximum size of a window's client area.

## Syntax

```c
void SDL_SetWindowMaximumSize(SDL_Window * window,
                              int max_w, int max_h);

```

## Function Parameters

|                |                                            |
| -------------- | ------------------------------------------ |
| **window**     | the window to change                       |
| **max_w**      | the maximum width of the window in pixels  |
| **max_h**      | the maximum height of the window in pixels |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize.md)
* [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize.md)

----
[CategoryAPI](CategoryAPI.md)
