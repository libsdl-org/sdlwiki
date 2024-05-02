###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickProperties

Get the properties associated with a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_PropertiesID SDL_GetJoystickProperties(SDL_Joystick *joystick);


#define SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN          "SDL.joystick.cap.mono_led"
#define SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN           "SDL.joystick.cap.rgb_led"
#define SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN        "SDL.joystick.cap.player_led"
#define SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN            "SDL.joystick.cap.rumble"
#define SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN    "SDL.joystick.cap.trigger_rumble"
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

## See Also

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

