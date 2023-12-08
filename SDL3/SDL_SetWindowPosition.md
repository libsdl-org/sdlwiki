###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowPosition

Request that the window's position be set.

## Syntax

```c
int SDL_SetWindowPosition(SDL_Window *window, int x, int y);

```

## Function Parameters

|                |                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window to reposition                                                                                                                      |
| **x**          | the x coordinate of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED) |
| **y**          | the y coordinate of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If, at the time of this request, the window is in a fixed-size state such
as maximized, this request may be deferred until the window returns to a
resizable state.

This can be used to reposition fullscreen-desktop windows onto a different
display, however, exclusive fullscreen windows are locked to a specific
display and can only be repositioned programmatically via
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode.md)().

On some windowing systems this request is asynchronous and the new
coordinates may not have have been applied immediately upon the return of
this function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow.md)() to block until the changes have taken
effect.

When the window position changes, an
[SDL_EVENT_WINDOW_MOVED](SDL_EVENT_WINDOW_MOVED.md) event will be emitted with
the window's new coordinates. Note that the new coordinates may not match
the exact coordinates requested, as some windowing systems can restrict the
position of the window in certain scenarios (e.g. constraining the position
so the window is always within desktop bounds). Additionally, as this is
just a request, it can be denied by the windowing system.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowPosition](SDL_GetWindowPosition.md)
* [SDL_SyncWindow](SDL_SyncWindow.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
