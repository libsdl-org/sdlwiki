###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MinimizeWindow

Request that the window be minimized to an iconic representation.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_MinimizeWindow(SDL_Window *window);
```

## Function Parameters

|                            |            |                         |
| -------------------------- | ---------- | ----------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to minimize. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

On some windowing systems this request is asynchronous and the new window
state may not have been applied immediately upon the return of this
function. If an immediate change is required, call
[SDL_SyncWindow](SDL_SyncWindow)() to block until the changes have taken
effect.

When the window state changes, an
[SDL_EVENT_WINDOW_MINIMIZED](SDL_EVENT_WINDOW_MINIMIZED) event will be
emitted. Note that, as this is just a request, the windowing system can
deny the state change.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_MaximizeWindow](SDL_MaximizeWindow)
- [SDL_RestoreWindow](SDL_RestoreWindow)
- [SDL_SyncWindow](SDL_SyncWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

