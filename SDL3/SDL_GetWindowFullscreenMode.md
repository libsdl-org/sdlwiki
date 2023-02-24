###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowFullscreenMode

Query the display mode to use when a window is visible at fullscreen.

## Syntax

```c
const SDL_DisplayMode* SDL_GetWindowFullscreenMode(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns a pointer to the fullscreen mode to use or NULL for desktop mode

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)

----
[CategoryAPI](CategoryAPI)

