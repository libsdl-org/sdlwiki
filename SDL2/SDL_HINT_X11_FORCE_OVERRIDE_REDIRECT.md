###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_X11_FORCE_OVERRIDE_REDIRECT

Mark X11 windows as override-redirect.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_X11_FORCE_OVERRIDE_REDIRECT "SDL_X11_FORCE_OVERRIDE_REDIRECT"
```

## Remarks

If set, this _might_ increase framerate at the expense of the desktop not
working as expected. Override-redirect windows aren't noticed by the window
manager at all.

You should probably only use this for fullscreen windows, and you probably
shouldn't even use it for that. But it's here if you want to try!

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

