# SDL_HINT_VIDEO_DISPLAY_PRIORITY

A comma separated list containing the names of the displays that SDL should sort to the front of the display list.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_DISPLAY_PRIORITY "SDL_VIDEO_DISPLAY_PRIORITY"
```

## Remarks

When this hint is set, displays with matching name strings will be
prioritized in the list of displays, as exposed by calling
[SDL_GetDisplays](SDL_GetDisplays)(), with the first listed becoming the
primary display. The naming convention can vary depending on the
environment, but it is usually a connector name (e.g. 'DP-1', 'DP-2',
'HDMI-A-1', etc...).

On Wayland desktops, the connector names associated with displays can be
found in the `name` property of the info output from `wayland-info -i
wl_output`. On X11 desktops, the `xrandr` utility can be used to retrieve
the connector names associated with displays.

This hint is currently supported on the following drivers:

- KMSDRM (kmsdrm)
- Wayland (wayland)
- X11 (x11)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

