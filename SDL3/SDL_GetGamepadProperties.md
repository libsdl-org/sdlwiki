###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadProperties

Get the properties associated with an opened gamepad.

## Syntax

```c
SDL_PropertiesID SDL_GetGamepadProperties(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

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

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

