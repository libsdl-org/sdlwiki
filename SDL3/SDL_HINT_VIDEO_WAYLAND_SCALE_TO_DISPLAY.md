###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WAYLAND_SCALE_TO_DISPLAY

A variable forcing non-DPI-aware Wayland windows to output at 1:1 scaling.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_SCALE_TO_DISPLAY "SDL_VIDEO_WAYLAND_SCALE_TO_DISPLAY"
```

## Remarks

This must be set before initializing the video subsystem.

When this hint is set, Wayland windows that are not flagged as being
DPI-aware will be output with scaling designed to force 1:1 pixel mapping.

This is intended to allow legacy applications to be displayed without
desktop scaling being applied, and has issues with certain display
configurations, as this forces the window to behave in a way that Wayland
desktops were not designed to accommodate:

- Rounding errors can result with odd window sizes and/or desktop scales,
  which can cause the window contents to appear slightly blurry.
- The window may be unusably small on scaled desktops.
- The window may jump in size when moving between displays of different
  scale factors.
- Displays may appear to overlap when using a multi-monitor setup with
  scaling enabled.
- Possible loss of cursor precision due to the logical size of the window
  being reduced.

New applications should be designed with proper DPI awareness handling
instead of enabling this.

The variable can be set to the following values:

- "0": Windows will be scaled normally.
- "1": Windows will be forced to scale to achieve 1:1 output.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

