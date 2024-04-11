###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ENABLE_STEAM_CONTROLLERS

A variable that controls whether Steam Controllers should be exposed using the SDL joystick and game controller APIs

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_ENABLE_STEAM_CONTROLLERS "SDL_ENABLE_STEAM_CONTROLLERS"
```

## Remarks

The variable can be set to the following values: "0" - Do not scan for
Steam Controllers "1" - Scan for Steam Controllers (the default)

The default value is "1". This hint must be set before initializing the
joystick subsystem.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

