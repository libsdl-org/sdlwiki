###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowMinimumSize

Get the minimum size of a window's client area.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_GetWindowMinimumSize(SDL_Window * window,
                          int *w, int *h);
```

## Function Parameters

|                            |            |                                                                         |
| -------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query.                                                    |
| int *                      | **w**      | a pointer filled in with the minimum width of the window, may be NULL.  |
| int *                      | **h**      | a pointer filled in with the minimum height of the window, may be NULL. |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

