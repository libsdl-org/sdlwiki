###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_PS2_DYNAMIC_VSYNC

A variable controlling if VSYNC is automatically disable if doesn't reach the enough FPS

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_PS2_DYNAMIC_VSYNC    "SDL_PS2_DYNAMIC_VSYNC"
```

## Remarks

This variable can be set to the following values:

- "0": It will be using VSYNC as defined in the main flag. Default
- "1": If VSYNC was previously enabled, then it will disable VSYNC if
  doesn't reach enough speed

By default SDL does not enable the automatic VSYNC

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

