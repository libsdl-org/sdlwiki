###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowMaximumSize

Set the maximum size of a window's client area.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowMaximumSize(SDL_Window * window,
                          int max_w, int max_h);
```

## Function Parameters

|                            |            |                                             |
| -------------------------- | ---------- | ------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                       |
| int                        | **max_w**  | the maximum width of the window in pixels.  |
| int                        | **max_h**  | the maximum height of the window in pixels. |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

