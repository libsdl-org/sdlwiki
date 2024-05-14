###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DetachVirtualJoystick

Detach a virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_DetachVirtualJoystick(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| **instance_id**     | the joystick instance ID, previously returned from [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)() |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

