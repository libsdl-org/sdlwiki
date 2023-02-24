###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowAlwaysOnTop

Set the window to always be above the others.

## Syntax

```c
int SDL_SetWindowAlwaysOnTop(SDL_Window *window, SDL_bool on_top);

```

## Function Parameters

|                |                                                                                         |
| -------------- | --------------------------------------------------------------------------------------- |
| **window**     | The window of which to change the always on top state                                   |
| **on_top**     | [SDL_TRUE](SDL_TRUE) to set the window always on top, [SDL_FALSE](SDL_FALSE) to disable |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_ALWAYS_ON_TOP`](SDL_WINDOW_ALWAYS_ON_TOP) flag. This will
bring the window to the front and keep the window above the rest.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI)

