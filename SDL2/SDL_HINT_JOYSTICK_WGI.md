###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_WGI

A variable controlling whether Windows.Gaming.Input should be used for controller handling.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_JOYSTICK_WGI "SDL_JOYSTICK_WGI"
```

## Remarks

This variable can be set to the following values: "0" - WGI is not used "1"
- WGI is used (the default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

