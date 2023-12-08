###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MaximizeWindow

Request that the window be made as large as possible.

## Syntax

```c
int SDL_MaximizeWindow(SDL_Window *window);

```

## Function Parameters

|                |                        |
| -------------- | ---------------------- |
| **window**     | the window to maximize |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Non-resizable windows can't be maximized. The window must have the
[SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE.md) flag set, or this will have no
effect.

On some windowing systems this request is asynchronous and the new window
state may not have have been applied immediately upon the return of this
function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow.md)() to block until the changes have taken
effect.

When the window state changes, an
[SDL_EVENT_WINDOW_MAXIMIZED](SDL_EVENT_WINDOW_MAXIMIZED.md) event will be
emitted. Note that, as this is just a request, the windowing system can
deny the state change.

When maximizing a window, whether the constraints set via
[SDL_SetWindowMaximumSize](SDL_SetWindowMaximumSize.md)() are honored depends
on the policy of the window manager. Win32 and macOS enforce the
constraints when maximizing, while X11 and Wayland window managers may
vary.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_MinimizeWindow](SDL_MinimizeWindow.md)
* [SDL_RestoreWindow](SDL_RestoreWindow.md)
* [SDL_SyncWindow](SDL_SyncWindow.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
