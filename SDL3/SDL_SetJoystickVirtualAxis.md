# SDL_SetJoystickVirtualAxis

Set the state of an axis on an opened virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SetJoystickVirtualAxis(SDL_Joystick *joystick, int axis, Sint16 value);
```

## Function Parameters

|                                |              |                                                          |
| ------------------------------ | ------------ | -------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the virtual joystick on which to set state.              |
| int                            | **axis**     | the index of the axis on the virtual joystick to update. |
| [Sint16](Sint16)               | **value**    | the new value for the specified axis.                    |

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

Note that when sending trigger axes, you should scale the value to the full
range of [Sint16](Sint16). For example, a trigger at rest would have the
value of [`SDL_JOYSTICK_AXIS_MIN`](SDL_JOYSTICK_AXIS_MIN).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetJoystickVirtualButton](SDL_SetJoystickVirtualButton)
- [SDL_SetJoystickVirtualBall](SDL_SetJoystickVirtualBall)
- [SDL_SetJoystickVirtualHat](SDL_SetJoystickVirtualHat)
- [SDL_SetJoystickVirtualTouchpad](SDL_SetJoystickVirtualTouchpad)
- [SDL_SetJoystickVirtualSensorData](SDL_SetJoystickVirtualSensorData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

