###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_DPI_SCALING

Uses DPI-scaled points as the SDL coordinate system on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_WINDOWS_DPI_SCALING "SDL_WINDOWS_DPI_SCALING"
```

## Remarks

This changes the SDL coordinate system units to be DPI-scaled points,
rather than pixels everywhere. This means windows will be appropriately
sized, even when created on high-DPI displays with scaling.

e.g. requesting a 640x480 window from SDL, on a display with 125% scaling
in Windows display settings, will create a window with an 800x600 client
area (in pixels).

Setting this to "1" implicitly requests process DPI awareness (setting
[SDL_WINDOWS_DPI_AWARENESS](SDL_WINDOWS_DPI_AWARENESS) is unnecessary), and
forces [SDL_WINDOW_ALLOW_HIGHDPI](SDL_WINDOW_ALLOW_HIGHDPI) on all windows.

This variable can be set to the following values: "0" - SDL coordinates
equal Windows coordinates. No automatic window resizing when dragging
between monitors with different scale factors (unless this is performed by
Windows itself, which is the case when the process is DPI unaware). "1" -
SDL coordinates are in DPI-scaled points. Automatically resize windows as
needed on displays with non-100% scale factors.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

