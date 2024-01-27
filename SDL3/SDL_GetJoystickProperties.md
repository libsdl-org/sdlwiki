###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickProperties

Get the properties associated with a joystick.

## Syntax

```c
SDL_PropertiesID SDL_GetJoystickProperties(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following read-only properties are provided by SDL:

- [`SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN`](SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN):
  true if this joystick has an LED that has adjustable brightness
- [`SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN`](SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN):
  true if this joystick has an LED that has adjustable color
- [`SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN`](SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN):
  true if this joystick has a player LED
- [`SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN`](SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN):
  true if this joystick has left/right rumble
- [`SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN`](SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN):
  true if this joystick has simple trigger rumble

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

