###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_KMSDRM_DEVICE_INDEX

A variable that decides what KMSDRM device to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_KMSDRM_DEVICE_INDEX "SDL_KMSDRM_DEVICE_INDEX"
```

## Remarks

Internally, SDL might open something like "/dev/dri/cardNN" to access
KMSDRM functionality, where "NN" is a device index number.

SDL makes a guess at the best index to use (usually zero), but the app or
user can set this hint to a number between 0 and 99 to force selection.

This hint is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

