###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_DPI_AWARENESS

Controls whether SDL will declare the process to be DPI aware.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_DPI_AWARENESS "SDL_WINDOWS_DPI_AWARENESS"
```

## Remarks

This hint must be set before initializing the video subsystem.

The main purpose of declaring DPI awareness is to disable OS bitmap scaling
of SDL windows on monitors with a DPI scale factor.

This hint is equivalent to requesting DPI awareness via external means
(e.g. calling SetProcessDpiAwarenessContext) and does not cause SDL to use
a virtualized coordinate system, so it will generally give you 1 SDL
coordinate = 1 pixel even on high-DPI displays.

For more information, see:
https://docs.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows

This variable can be set to the following values:

- "": Do not change the DPI awareness (default).
- "unaware": Declare the process as DPI unaware. (Windows 8.1 and later).
- "system": Request system DPI awareness. (Vista and later).
- "permonitor": Request per-monitor DPI awareness. (Windows 8.1 and later).
- "permonitorv2": Request per-monitor V2 DPI awareness. (Windows 10,
  version 1607 and later). The most visible difference from "permonitor" is
  that window title bar will be scaled to the visually correct size when
  dragging between monitors with different scale factors. This is the
  preferred DPI awareness level.

If the requested DPI awareness is not available on the currently running
OS, SDL will try to request the best available match.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

