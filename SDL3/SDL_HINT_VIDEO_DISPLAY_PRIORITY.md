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
'HDMI-A-1',etc...).

On Wayland and X11 desktops, the connector names associated with displays
can typically be found by using the `xrandr` utility.

This hint is currently supported on the following drivers:

- KMSDRM (kmsdrm)
- Wayland (wayland)
- X11 (x11)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

