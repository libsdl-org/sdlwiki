###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WAYLAND_MODE_SCALING

A variable controlling how modes with a non-native aspect ratio are displayed under Wayland.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_MODE_SCALING "SDL_VIDEO_WAYLAND_MODE_SCALING"
```

## Remarks

When this hint is set, the requested scaling will be used when displaying
fullscreen video modes that don't match the display's native aspect ratio.
This is contingent on compositor viewport support.

The variable can be set to the following values:

- "aspect" - Video modes will be displayed scaled, in their proper aspect
  ratio, with black bars.
- "stretch" - Video modes will be scaled to fill the entire display.
  (default)
- "none" - Video modes will be displayed as 1:1 with no scaling.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

