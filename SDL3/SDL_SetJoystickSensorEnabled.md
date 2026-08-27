# SDL_SetJoystickSensorEnabled

Set whether data reporting for a joystick sensor is enabled.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SetJoystickSensorEnabled(SDL_Joystick *joystick, SDL_SensorType type, bool enabled);
```

## Function Parameters

|                                  |              |                                           |
| -------------------------------- | ------------ | ----------------------------------------- |
| [SDL_Joystick](SDL_Joystick) *   | **joystick** | the joystick to update.                   |
| [SDL_SensorType](SDL_SensorType) | **type**     | the type of sensor to enable/disable.     |
| bool                             | **enabled**  | whether data reporting should be enabled. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Sensors are disabled by default and this function is used to enable them.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_JoystickHasSensor](SDL_JoystickHasSensor)
- [SDL_JoystickSensorEnabled](SDL_JoystickSensorEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

