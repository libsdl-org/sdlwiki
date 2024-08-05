###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_X11_NODIRECTCOLOR

A variable controlling whether SDL uses DirectColor visuals.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_NODIRECTCOLOR "SDL_VIDEO_X11_NODIRECTCOLOR"
```

## Remarks

The variable can be set to the following values:

- "0": Disable DirectColor visuals.
- "1": Enable DirectColor visuals. (default)

This hint should be set before initializing the video subsystem.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

