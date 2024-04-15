###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WAYLAND_MODE_EMULATION

A variable controlling whether video mode emulation is enabled under Wayland.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_MODE_EMULATION "SDL_VIDEO_WAYLAND_MODE_EMULATION"
```

## Remarks

When this hint is set, a standard set of emulated CVT video modes will be
exposed for use by the application. If it is disabled, the only modes
exposed will be the logical desktop size and, in the case of a scaled
desktop, the native display resolution.

The variable can be set to the following values:

- "0": Video mode emulation is disabled.
- "1": Video mode emulation is enabled. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

