# SDL_SetWindowPosition

Request that the window's position be set.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowPosition(SDL_Window *window, int x, int y);
```

## Function Parameters

|                            |            |                                                                                                                                                |
| -------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to reposition.                                                                                                                      |
| int                        | **x**      | the x coordinate of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). |
| int                        | **y**      | the y coordinate of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the window is in an exclusive fullscreen or maximized state, this
request has no effect.

This can be used to reposition fullscreen-desktop windows onto a different
display, however, as exclusive fullscreen windows are locked to a specific
display, they can only be repositioned programmatically via
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)().

On some windowing systems this request is asynchronous and the new
coordinates may not have have been applied immediately upon the return of
this function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow)() to block until the changes have taken
effect.

When the window position changes, an
[SDL_EVENT_WINDOW_MOVED](SDL_EVENT_WINDOW_MOVED) event will be emitted with
the window's new coordinates. Note that the new coordinates may not match
the exact coordinates requested, as some windowing systems can restrict the
position of the window in certain scenarios (e.g. constraining the position
so the window is always within desktop bounds). Additionally, as this is
just a request, it can be denied by the windowing system.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowPosition](SDL_GetWindowPosition)
- [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

