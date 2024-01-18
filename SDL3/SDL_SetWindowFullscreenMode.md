###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowFullscreenMode

Set the display mode to use when a window is visible and fullscreen.

## Syntax

```c
int SDL_SetWindowFullscreenMode(SDL_Window *window, const SDL_DisplayMode *mode);

```

## Function Parameters

|                |                                                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **window**     | the window to affect                                                                                                                                                                                                                             |
| **mode**       | a pointer to the display mode to use, which can be NULL for borderless fullscreen desktop mode, or one of the fullscreen modes returned by [SDL_GetFullscreenDisplayModes](SDL_GetFullscreenDisplayModes)() to set an exclusive fullscreen mode. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This only affects the display mode used when the window is fullscreen. To
change the window size when the window is not fullscreen, use
[SDL_SetWindowSize](SDL_SetWindowSize)().

If the window is currently in the fullscreen state, this request is
asynchronous on some windowing systems and the new mode dimensions may not
be applied immediately upon the return of this function. If an immediate
change is required, call [SDL_SyncWindow](SDL_SyncWindow)() to block until
the changes have taken effect.

When the new mode takes effect, an
[SDL_EVENT_WINDOW_RESIZED](SDL_EVENT_WINDOW_RESIZED) and/or an
[SDL_EVENT_WINDOOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOOW_PIXEL_SIZE_CHANGED)
event will be emitted with the new mode dimensions.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)
* [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI)

