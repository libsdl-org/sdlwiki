# SDL_SetWindowFullscreen

Request that the window's fullscreen state be changed.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowFullscreen(SDL_Window *window, bool fullscreen);
```

## Function Parameters

|                            |                |                                                    |
| -------------------------- | -------------- | -------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**     | the window to change.                              |
| bool                       | **fullscreen** | true for fullscreen mode, false for windowed mode. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

By default a window in fullscreen state uses borderless fullscreen desktop
mode, but a specific exclusive display mode can be set using
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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
- [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
- [SDL_SyncWindow](SDL_SyncWindow)
- [SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

