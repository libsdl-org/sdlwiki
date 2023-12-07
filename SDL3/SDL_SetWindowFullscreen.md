###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowFullscreen

Request that the window's fullscreen state be changed.

## Syntax

```c
int SDL_SetWindowFullscreen(SDL_Window *window, SDL_bool fullscreen);

```

## Function Parameters

|                    |                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------- |
| **window**         | the window to change                                                               |
| **fullscreen**     | [SDL_TRUE](SDL_TRUE) for fullscreen mode, [SDL_FALSE](SDL_FALSE) for windowed mode |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

By default a window in fullscreen state uses fullscreen desktop mode, but a
specific display mode can be set using
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)().

On some windowing systems this request is asynchronous and the new
fullscreen state may not have have been applied immediately upon the return
of this function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow)() to block until the changes have taken
effect.

When the window state changes, an
[SDL_EVENT_WINDOW_ENTER_FULLSCREEN](SDL_EVENT_WINDOW_ENTER_FULLSCREEN) or
[SDL_EVENT_WINDOW_LEAVE_FULLSCREEN](SDL_EVENT_WINDOW_LEAVE_FULLSCREEN)
event will be emitted. Note that, as this is just a request, it can be
denied by the windowing system.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
* [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
* [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


