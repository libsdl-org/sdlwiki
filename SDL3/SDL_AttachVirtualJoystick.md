# SDL_AttachVirtualJoystick

Attach a new virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickID SDL_AttachVirtualJoystick(const SDL_VirtualJoystickDesc *desc);
```

## Function Parameters

|                                                            |          |                                                                                     |
| ---------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| const [SDL_VirtualJoystickDesc](SDL_VirtualJoystickDesc) * | **desc** | joystick description, initialized using [SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)(). |

## Return Value

([SDL_JoystickID](SDL_JoystickID)) Returns the joystick instance ID, or 0
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Apps can create virtual joysticks, that exist without hardware directly
backing them, and have program-supplied inputs. Once attached, a virtual
joystick looks like any other joystick that SDL can access. These can be
used to make other things look like joysticks, or provide pre-recorded
input, etc.

Once attached, the app can send joystick inputs to the new virtual joystick
using [SDL_SetJoystickVirtualAxis](SDL_SetJoystickVirtualAxis)(), etc.

When no longer needed, the virtual joystick can be removed by calling
[SDL_DetachVirtualJoystick](SDL_DetachVirtualJoystick)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DetachVirtualJoystick](SDL_DetachVirtualJoystick)
- [SDL_SetJoystickVirtualAxis](SDL_SetJoystickVirtualAxis)
- [SDL_SetJoystickVirtualButton](SDL_SetJoystickVirtualButton)
- [SDL_SetJoystickVirtualBall](SDL_SetJoystickVirtualBall)
- [SDL_SetJoystickVirtualHat](SDL_SetJoystickVirtualHat)
- [SDL_SetJoystickVirtualTouchpad](SDL_SetJoystickVirtualTouchpad)
- [SDL_SetJoystickVirtualSensorData](SDL_SetJoystickVirtualSensorData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

