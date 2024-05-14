###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_X11_NET_WM_PING

A variable controlling whether the X11 _NET_WM_PING protocol should be supported.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_NET_WM_PING      "SDL_VIDEO_X11_NET_WM_PING"
```

## Remarks

By default SDL will use _NET_WM_PING, but for applications that know they
will not always be able to respond to ping requests in a timely manner they
can turn it off to avoid the window manager thinking the app is hung.

The variable can be set to the following values:

- "0": Disable _NET_WM_PING.
- "1": Enable _NET_WM_PING. (default)

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

