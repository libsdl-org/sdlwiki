###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_SYNC_WINDOW_OPERATIONS

A variable controlling whether all window operations will block until complete.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_SYNC_WINDOW_OPERATIONS "SDL_VIDEO_SYNC_WINDOW_OPERATIONS"
```

## Remarks

Window systems that run asynchronously may not have the results of window
operations that resize or move the window applied immediately upon the
return of the requesting function. Setting this hint will cause such
operations to block after every call until the pending operation has
completed. Setting this to '1' is the equivalent of calling
[SDL_SyncWindow](SDL_SyncWindow)() after every function call.

Be aware that amount of time spent blocking while waiting for window
operations to complete can be quite lengthy, as animations may have to
complete, which can take upwards of multiple seconds in some cases.

The variable can be set to the following values:

- "0": Window operations are non-blocking. (default)
- "1": Window operations will block until completed.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

