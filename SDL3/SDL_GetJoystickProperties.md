# SDL_GetJoystickProperties

Get the properties associated with a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_PropertiesID SDL_GetJoystickProperties(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                                        |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)(). |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

