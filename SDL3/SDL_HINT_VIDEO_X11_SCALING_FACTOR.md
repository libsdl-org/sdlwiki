###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_VIDEO_X11_SCALING_FACTOR

A variable forcing the content scaling factor for X11 displays.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_SCALING_FACTOR "SDL_VIDEO_X11_SCALING_FACTOR"
```

## Remarks

The variable can be set to a floating point value in the range 1.0-10.0f

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

