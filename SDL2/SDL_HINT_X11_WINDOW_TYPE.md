###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_X11_WINDOW_TYPE

A variable that forces X11 windows to create as a custom type.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_X11_WINDOW_TYPE "SDL_X11_WINDOW_TYPE"
```

## Remarks

This is currently only used for X11 and ignored elsewhere.

During [SDL_CreateWindow](SDL_CreateWindow), SDL uses the
_NET_WM_WINDOW_TYPE X11 property to report to the window manager the type
of window it wants to create. This might be set to various things if
[SDL_WINDOW_TOOLTIP](SDL_WINDOW_TOOLTIP) or
[SDL_WINDOW_POPUP_MENU](SDL_WINDOW_POPUP_MENU), etc, were specified. For
"normal" windows that haven't set a specific type, this hint can be used to
specify a custom type. For example, a dock window might set this to
"_NET_WM_WINDOW_TYPE_DOCK".

If not set or set to "", this hint is ignored. This hint must be set before
the [SDL_CreateWindow](SDL_CreateWindow)() call that it is intended to
affect.

This hint is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

