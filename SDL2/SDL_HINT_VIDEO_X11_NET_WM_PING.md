###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_X11_NET_WM_PING

A variable controlling whether the X11 _NET_WM_PING protocol should be supported.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_NET_WM_PING      "SDL_VIDEO_X11_NET_WM_PING"
```

## Remarks

This variable can be set to the following values:

- "0": Disable _NET_WM_PING
- "1": Enable _NET_WM_PING

By default SDL will use _NET_WM_PING, but for applications that know they
will not always be able to respond to ping requests in a timely manner they
can turn it off to avoid the window manager thinking the app is hung. The
hint is checked in CreateWindow.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


