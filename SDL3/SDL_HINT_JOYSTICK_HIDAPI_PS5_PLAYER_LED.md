# SDL_HINT_JOYSTICK_HIDAPI_PS5_PLAYER_LED

A variable controlling whether the player LEDs should be lit to indicate which player is associated with a PS5 controller.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS5_PLAYER_LED "SDL_JOYSTICK_HIDAPI_PS5_PLAYER_LED"
```

## Remarks

The variable can be set to the following values:

- "0": player LEDs are not enabled.
- "1": player LEDs are enabled. (default)

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

