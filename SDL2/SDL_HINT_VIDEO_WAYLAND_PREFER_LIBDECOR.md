# SDL_HINT_VIDEO_WAYLAND_PREFER_LIBDECOR

A variable controlling whether the libdecor Wayland backend is preferred over native decorations.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_PREFER_LIBDECOR "SDL_VIDEO_WAYLAND_PREFER_LIBDECOR"
```

## Remarks

When this hint is set, libdecor will be used to provide window decorations,
even if xdg-decoration is available. (Note that, by default, libdecor will
use xdg-decoration itself if available).

This variable can be set to the following values:

- "0": libdecor is enabled only if server-side decorations are unavailable.
- "1": libdecor is always enabled if available.

libdecor is used over xdg-shell when xdg-decoration protocol is
unavailable.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

