# SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR

A variable controlling whether the X11 _NET_WM_BYPASS_COMPOSITOR hint should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR "SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR"
```

## Remarks

This variable can be set to the following values:

- "0": Disable _NET_WM_BYPASS_COMPOSITOR
- "1": Enable _NET_WM_BYPASS_COMPOSITOR

By default SDL will use _NET_WM_BYPASS_COMPOSITOR

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

