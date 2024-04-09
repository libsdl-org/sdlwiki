###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_X11_FORCE_OVERRIDE_REDIRECT

A variable controlling whether X11 windows are marked as override-redirect.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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

The variable can be set to the following values:

- "0": Do not mark the window as override-redirect. (default)
- "1": Mark the window as override-redirect.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

