###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_X11_WINDOW_TYPE

A variable specifying the type of an X11 window.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_X11_WINDOW_TYPE "SDL_X11_WINDOW_TYPE"
```

## Remarks

During [SDL_CreateWindow](SDL_CreateWindow), SDL uses the
_NET_WM_WINDOW_TYPE X11 property to report to the window manager the type
of window it wants to create. This might be set to various things if
[SDL_WINDOW_TOOLTIP](SDL_WINDOW_TOOLTIP) or
[SDL_WINDOW_POPUP_MENU](SDL_WINDOW_POPUP_MENU), etc, were specified. For
"normal" windows that haven't set a specific type, this hint can be used to
specify a custom type. For example, a dock window might set this to
"_NET_WM_WINDOW_TYPE_DOCK".

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

