###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SyncWindow

Block until any pending window state is finalized.

## Syntax

```c
int SDL_SyncWindow(SDL_Window *window);

```

## Function Parameters

|                |                                                                  |
| -------------- | ---------------------------------------------------------------- |
| **window**     | the window for which to wait for the pending state to be applied |

## Return Value

Returns 0 on success, a positive value if the operation timed out before
the window was in the requested state, or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

On asynchronous windowing systems, this acts as a synchronization barrier
for pending window state. It will attempt to wait until any pending window
state has been applied and is guaranteed to return within finite time. Note
that for how long it can potentially block depends on the underlying window
system, as window state changes may involve somewhat lengthy animations
that must complete before the window is in its final requested state.

On windowing systems where changes are immediate, this does nothing.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowSize](SDL_SetWindowSize)
* [SDL_SetWindowPosition](SDL_SetWindowPosition)
* [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)
* [SDL_MinimizeWindow](SDL_MinimizeWindow)
* [SDL_MaximizeWindow](SDL_MaximizeWindow)
* [SDL_RestoreWindow](SDL_RestoreWindow)

----
[CategoryAPI](CategoryAPI)

