###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_KMSDRM_DEVICE_INDEX

A variable that controls what KMSDRM device to use.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_KMSDRM_DEVICE_INDEX "SDL_KMSDRM_DEVICE_INDEX"
```

## Remarks

SDL might open something like "/dev/dri/cardNN" to access KMSDRM
functionality, where "NN" is a device index number. SDL makes a guess at
the best index to use (usually zero), but the app or user can set this hint
to a number between 0 and 99 to force selection.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

