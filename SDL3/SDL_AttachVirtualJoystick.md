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

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DetachVirtualJoystick](SDL_DetachVirtualJoystick)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

