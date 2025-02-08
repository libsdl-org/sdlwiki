# SDL_HINT_VIDEO_WAYLAND_ALLOW_LIBDECOR

A variable controlling whether the libdecor Wayland backend is allowed to be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_ALLOW_LIBDECOR "SDL_VIDEO_WAYLAND_ALLOW_LIBDECOR"
```

## Remarks

This variable can be set to the following values:

- "0": libdecor use is disabled.
- "1": libdecor use is enabled (default).

libdecor is used over xdg-shell when xdg-decoration protocol is
unavailable.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

