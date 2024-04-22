###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_WAYLAND_MODE_EMULATION

A variable controlling whether video mode emulation is enabled under Wayland.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_MODE_EMULATION "SDL_VIDEO_WAYLAND_MODE_EMULATION"
```

## Remarks

When this hint is set, a standard set of emulated CVT video modes will be
exposed for use by the application. If it is disabled, the only modes
exposed will be the logical desktop size and, in the case of a scaled
desktop, the native display resolution.

This variable can be set to the following values: "0" - Video mode
emulation is disabled. "1" - Video mode emulation is enabled.

By default video mode emulation is enabled.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

