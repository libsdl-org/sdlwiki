###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DetachVirtualJoystick

Detach a virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_DetachVirtualJoystick(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                                                                                                              |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------ |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID, previously returned from [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)(). |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

