###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowFullscreenMode

Set the display mode to use when a window is visible and fullscreen.

## Syntax

```c
int SDL_SetWindowFullscreenMode(SDL_Window *window, const SDL_DisplayMode *mode);

```

## Function Parameters

|                |                                                                                                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window to affect                                                                                                                                                                   |
| **mode**       | a pointer to the display mode to use, which can be NULL for desktop mode, or one of the fullscreen modes returned by [SDL_GetFullscreenDisplayModes](SDL_GetFullscreenDisplayModes)(). |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This only affects the display mode used when the window is fullscreen. To
change the window size when the window is not fullscreen, use
[SDL_SetWindowSize](SDL_SetWindowSize)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)

----
[CategoryAPI](CategoryAPI)

