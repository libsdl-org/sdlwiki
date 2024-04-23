###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUTO_UPDATE_JOYSTICKS

A variable controlling whether SDL updates joystick state when getting input events

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUTO_UPDATE_JOYSTICKS  "SDL_AUTO_UPDATE_JOYSTICKS"
```

## Remarks

This variable can be set to the following values:

- "0": You'll call [SDL_JoystickUpdate](SDL_JoystickUpdate)() manually
- "1": SDL will automatically call
  [SDL_JoystickUpdate](SDL_JoystickUpdate)() (default)

This hint can be toggled on and off at runtime.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

