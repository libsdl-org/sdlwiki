# SDL_GetGamepadProperties

Get the properties associated with an opened gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_PropertiesID SDL_GetGamepadProperties(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                                                                                   |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)(). |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

These properties are shared with the underlying joystick object.

The following read-only properties are provided by SDL:

- [`SDL_PROP_GAMEPAD_CAP_MONO_LED_BOOLEAN`](SDL_PROP_GAMEPAD_CAP_MONO_LED_BOOLEAN):
  true if this gamepad has an LED that has adjustable brightness
- [`SDL_PROP_GAMEPAD_CAP_RGB_LED_BOOLEAN`](SDL_PROP_GAMEPAD_CAP_RGB_LED_BOOLEAN):
  true if this gamepad has an LED that has adjustable color
- [`SDL_PROP_GAMEPAD_CAP_PLAYER_LED_BOOLEAN`](SDL_PROP_GAMEPAD_CAP_PLAYER_LED_BOOLEAN):
  true if this gamepad has a player LED
- [`SDL_PROP_GAMEPAD_CAP_RUMBLE_BOOLEAN`](SDL_PROP_GAMEPAD_CAP_RUMBLE_BOOLEAN):
  true if this gamepad has left/right rumble
- [`SDL_PROP_GAMEPAD_CAP_TRIGGER_RUMBLE_BOOLEAN`](SDL_PROP_GAMEPAD_CAP_TRIGGER_RUMBLE_BOOLEAN):
  true if this gamepad has simple trigger rumble

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

