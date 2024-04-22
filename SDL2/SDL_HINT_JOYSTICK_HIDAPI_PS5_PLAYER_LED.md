###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_PS5_PLAYER_LED

A variable controlling whether the player LEDs should be lit to indicate which player is associated with a PS5 controller.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS5_PLAYER_LED "SDL_JOYSTICK_HIDAPI_PS5_PLAYER_LED"
```

## Remarks

This variable can be set to the following values: "0" - player LEDs are not
enabled "1" - player LEDs are enabled (the default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

