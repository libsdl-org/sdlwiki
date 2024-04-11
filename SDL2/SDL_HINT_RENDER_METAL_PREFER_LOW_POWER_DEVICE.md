###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_METAL_PREFER_LOW_POWER_DEVICE

A variable controlling whether the Metal render driver select low power device over default one

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_RENDER_METAL_PREFER_LOW_POWER_DEVICE "SDL_RENDER_METAL_PREFER_LOW_POWER_DEVICE"
```

## Remarks

This variable can be set to the following values: "0" - Use the prefered OS
device "1" - Select a low power one

By default the prefered OS device is used.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

