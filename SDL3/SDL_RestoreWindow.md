###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RestoreWindow

Request that the size and position of a minimized or maximized window be restored.

## Syntax

```c
int SDL_RestoreWindow(SDL_Window *window);

```

## Function Parameters

|                |                       |
| -------------- | --------------------- |
| **window**     | the window to restore |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

On some windowing systems this request is asynchronous and the new window
state may not have have been applied immediately upon the return of this
function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow.md)() to block until the changes have taken
effect.

When the window state changes, an
[SDL_EVENT_WINDOW_RESTORED](SDL_EVENT_WINDOW_RESTORED.md) event will be
emitted. Note that, as this is just a request, the windowing system can
deny the state change.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_MaximizeWindow](SDL_MaximizeWindow.md)
* [SDL_MinimizeWindow](SDL_MinimizeWindow.md)
* [SDL_SyncWindow](SDL_SyncWindow.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
