# SDL_PROP_GLOBAL_VIDEO_WAYLAND_SESSION_ID_STRING

The session ID string used for saving and restoring window state across runs.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_PROP_GLOBAL_VIDEO_WAYLAND_SESSION_ID_STRING "SDL.video.wayland.session_id"
```

## Remarks

This requires that the compositor supports the `xdg_session_management_v1`
protocol.

To save and restore the current state of Wayland toplevel windows, set this
to a non-null value before creating a window, and serialize this value
before shutting down. To restore the previous state on subsequent runs, set
this property to the previously serialized value before window creation.

This can be set at any time before the first call to a window creation
function. Reading should be deferred until serialization time, as
compositors may not set the session identifier string immediately, and the
identifier string may change during runtime, so it should not be cached.

Setting this to an empty string ("") before creating a window will cause a
new session with an automatically generated identifier string to be
created.

Setting this to null or an empty string before shutting down the video
subsystem will cause the existing session to be removed.

Note that for windows to be saved/restored by the session, they also need a
stable, unique identifier string set via the
[`SDL_PROP_WINDOW_CREATE_WAYLAND_WINDOW_ID_STRING`](SDL_PROP_WINDOW_CREATE_WAYLAND_WINDOW_ID_STRING)
property at creation time.

## Version

This property is available since SDL 3.6.0.

## See Also

- [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

