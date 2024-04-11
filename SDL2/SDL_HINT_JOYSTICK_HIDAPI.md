###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI

A variable controlling whether the HIDAPI joystick drivers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI "SDL_JOYSTICK_HIDAPI"
```

## Remarks

This variable can be set to the following values: "0" - HIDAPI drivers are
not used "1" - HIDAPI drivers are used (the default)

This variable is the default for all drivers, but can be overridden by the
hints for specific drivers below.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

