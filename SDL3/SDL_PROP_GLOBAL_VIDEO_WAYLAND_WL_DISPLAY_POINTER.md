# SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER

The pointer to the global `wl_display` object used by the Wayland video backend.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER "SDL.video.wayland.wl_display"
```

## Remarks

Can be set before the video subsystem is initialized to import an external
`wl_display` object from an application or toolkit for use in SDL, or read
after initialization to export the `wl_display` used by the Wayland video
backend. Setting this property after the video subsystem has been
initialized has no effect, and reading it when the video subsystem is
uninitialized will either return the user provided value, if one was set
prior to initialization, or NULL. See docs/README-wayland.md for more
information.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

