# SDL_SetJoystickVirtualHat

Set the state of a hat on an opened virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SetJoystickVirtualHat(SDL_Joystick *joystick, int hat, Uint8 value);
```

## Function Parameters

|                                |              |                                                         |
| ------------------------------ | ------------ | ------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the virtual joystick on which to set state.             |
| int                            | **hat**      | the index of the hat on the virtual joystick to update. |
| Uint8                          | **value**    | the new value for the specified hat.                    |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Please note that values set here will not be applied until the next call to
[SDL_UpdateJoysticks](SDL_UpdateJoysticks), which can either be called
directly, or can be called indirectly through various other SDL APIs,
including, but not limited to the following:
[SDL_PollEvent](SDL_PollEvent), [SDL_PumpEvents](SDL_PumpEvents),
[SDL_WaitEventTimeout](SDL_WaitEventTimeout),
[SDL_WaitEvent](SDL_WaitEvent).

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetJoystickVirtualAxis](SDL_SetJoystickVirtualAxis)
- [SDL_SetJoystickVirtualButton](SDL_SetJoystickVirtualButton)
- [SDL_SetJoystickVirtualBall](SDL_SetJoystickVirtualBall)
- [SDL_SetJoystickVirtualTouchpad](SDL_SetJoystickVirtualTouchpad)
- [SDL_SetJoystickVirtualSensorData](SDL_SetJoystickVirtualSensorData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

