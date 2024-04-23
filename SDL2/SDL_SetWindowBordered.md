###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowBordered

Set the border state of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowBordered(SDL_Window * window,
                           SDL_bool bordered);

```

## Function Parameters

|                  |                                                                             |
| ---------------- | --------------------------------------------------------------------------- |
| **window**       | the window of which to change the border state                              |
| **bordered**     | [SDL_FALSE](SDL_FALSE) to remove border, [SDL_TRUE](SDL_TRUE) to add border |

## Remarks

This will add or remove the window's
[`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS) flag and add or remove the
border from the actual window. This is a no-op if the window's border
already matches the requested state.

You can't change the border state of a fullscreen window.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


