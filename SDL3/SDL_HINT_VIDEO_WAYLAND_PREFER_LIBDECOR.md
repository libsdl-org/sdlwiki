###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WAYLAND_PREFER_LIBDECOR

A variable controlling whether the libdecor Wayland backend is preferred over native decrations.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_PREFER_LIBDECOR "SDL_VIDEO_WAYLAND_PREFER_LIBDECOR"
```

## Remarks

When this hint is set, libdecor will be used to provide window decorations,
even if xdg-decoration is available. (Note that, by default, libdecor will
use xdg-decoration itself if available).

The variable can be set to the following values:

- "0": libdecor is enabled only if server-side decorations are unavailable.
  (default)
- "1": libdecor is always enabled if available.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

