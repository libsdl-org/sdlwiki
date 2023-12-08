###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowResizable

Set the user-resizable state of a window.

## Syntax

```c
void SDL_SetWindowResizable(SDL_Window * window,
                            SDL_bool resizable);

```

## Function Parameters

|                   |                                                                            |
| ----------------- | -------------------------------------------------------------------------- |
| **window**        | the window of which to change the resizable state                          |
| **resizable**     | [SDL_TRUE](SDL_TRUE.md) to allow resizing, [SDL_FALSE](SDL_FALSE.md) to disallow |

## Remarks

This will add or remove the window's
[`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE) flag and allow/disallow user
resizing of the window. This is a no-op if the window's resizable state
already matches the requested state.

You can't change the resizable state of a fullscreen window.

## Version

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags.md)

----
[CategoryAPI](CategoryAPI.md)
