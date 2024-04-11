###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_ROG_CHAKRAM

A variable controlling whether the ROG Chakram mice should show up as joysticks

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_JOYSTICK_ROG_CHAKRAM "SDL_JOYSTICK_ROG_CHAKRAM"
```

## Remarks

This variable can be set to the following values: "0" - ROG Chakram mice do
not show up as joysticks (the default) "1" - ROG Chakram mice show up as
joysticks

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

