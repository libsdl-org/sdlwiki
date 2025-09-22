# SDL_SetGamepadSensorEnabled

Set whether data reporting for a gamepad sensor is enabled.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_SetGamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type, bool enabled);
```

## Function Parameters

|                                  |             |                                           |
| -------------------------------- | ----------- | ----------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *     | **gamepad** | the gamepad to update.                    |
| [SDL_SensorType](SDL_SensorType) | **type**    | the type of sensor to enable/disable.     |
| bool                             | **enabled** | whether data reporting should be enabled. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GamepadHasSensor](SDL_GamepadHasSensor)
- [SDL_GamepadSensorEnabled](SDL_GamepadSensorEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

