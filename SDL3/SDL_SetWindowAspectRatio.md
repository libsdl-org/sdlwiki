###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowAspectRatio

Request that the aspect ratio of a window's client area be set.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowAspectRatio(SDL_Window *window, float min_aspect, float max_aspect);

```

## Function Parameters

|                    |                                                              |
| ------------------ | ------------------------------------------------------------ |
| **window**         | the window to change                                         |
| **min_aspect**     | the minimum aspect ratio of the window, or 0.0f for no limit |
| **max_aspect**     | the maximum aspect ratio of the window, or 0.0f for no limit |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The aspect ratio is the ratio of width divided by height, e.g. 2560x1600
would be 1.6. Larger aspect ratios are wider and smaller aspect ratios are
narrower.

If, at the time of this request, the window in a fixed-size state, such as
maximized or fullscreen, the request will be deferred until the window
exits this state and becomes resizable again.

On some windowing systems, this request is asynchronous and the new window
aspect ratio may not have have been applied immediately upon the return of
this function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow)() to block until the changes have taken
effect.

When the window size changes, an
[SDL_EVENT_WINDOW_RESIZED](SDL_EVENT_WINDOW_RESIZED) event will be emitted
with the new window dimensions. Note that the new dimensions may not match
the exact aspect ratio requested, as some windowing systems can restrict
the window size in certain scenarios (e.g. constraining the size of the
content area to remain within the usable desktop bounds). Additionally, as
this is just a request, it can be denied by the windowing system.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowAspectRatio](SDL_GetWindowAspectRatio)
- [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

