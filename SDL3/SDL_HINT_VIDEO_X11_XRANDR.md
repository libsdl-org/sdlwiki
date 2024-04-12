###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_X11_XRANDR

A variable controlling whether the X11 XRandR extension should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_VIDEO_X11_XRANDR           "SDL_VIDEO_X11_XRANDR"
```

## Remarks

The variable can be set to the following values:

- "0": Disable XRandR.
- "1": Enable XRandR. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


