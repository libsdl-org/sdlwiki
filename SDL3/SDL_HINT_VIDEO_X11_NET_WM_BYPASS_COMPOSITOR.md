###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR

A variable controlling whether the X11 _NET_WM_BYPASS_COMPOSITOR hint should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR "SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR"
```

## Remarks

The variable can be set to the following values:

- "0": Disable _NET_WM_BYPASS_COMPOSITOR.
- "1": Enable _NET_WM_BYPASS_COMPOSITOR. (default)

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

