###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowAlwaysOnTop

Set the window to always be above the others.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowAlwaysOnTop(SDL_Window * window,
                          SDL_bool on_top);
```

## Function Parameters

|                            |            |                                                                                         |
| -------------------------- | ---------- | --------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | The window of which to change the always on top state                                   |
| [SDL_bool](SDL_bool)       | **on_top** | [SDL_TRUE](SDL_TRUE) to set the window always on top, [SDL_FALSE](SDL_FALSE) to disable |

## Remarks

This will add or remove the window's
[`SDL_WINDOW_ALWAYS_ON_TOP`](SDL_WINDOW_ALWAYS_ON_TOP) flag. This will
bring the window to the front and keep the window above the rest.

## Version

This function is available since SDL 2.0.16.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

