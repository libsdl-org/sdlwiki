###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowAlwaysOnTop

Set the window to always be above the others.

## Syntax

```c
void SDL_SetWindowAlwaysOnTop(SDL_Window * window,
                              SDL_bool on_top);

```

## Function Parameters

|                |                                                                                         |
| -------------- | --------------------------------------------------------------------------------------- |
| **window**     | The window of which to change the always on top state                                   |
| **on_top**     | [SDL_TRUE](SDL_TRUE) to set the window always on top, [SDL_FALSE](SDL_FALSE) to disable |

## Remarks

This will add or remove the window's
[`SDL_WINDOW_ALWAYS_ON_TOP`](SDL_WINDOW_ALWAYS_ON_TOP) flag. This will
bring the window to the front and keep the window above the rest.

## Version

This function is available since SDL 2.0.16.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI)

