###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowSize

Request that the size of a window's client area be set.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowSize(SDL_Window *window, int w, int h);
```

## Function Parameters

|                            |            |                                        |
| -------------------------- | ---------- | -------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                  |
| int                        | **w**      | the width of the window, must be > 0.  |
| int                        | **h**      | the height of the window, must be > 0. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If, at the time of this request, the window in a fixed-size state, such as
maximized or fullscreen, the request will be deferred until the window
exits this state and becomes resizable again.

To change the fullscreen mode of a window, use
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)()

On some windowing systems, this request is asynchronous and the new window
size may not have have been applied immediately upon the return of this
function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow)() to block until the changes have taken
effect.

When the window size changes, an
[SDL_EVENT_WINDOW_RESIZED](SDL_EVENT_WINDOW_RESIZED) event will be emitted
with the new window dimensions. Note that the new dimensions may not match
the exact size requested, as some windowing systems can restrict the window
size in certain scenarios (e.g. constraining the size of the content area
to remain within the usable desktop bounds). Additionally, as this is just
a request, it can be denied by the windowing system.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowSize](SDL_GetWindowSize)
- [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
- [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

