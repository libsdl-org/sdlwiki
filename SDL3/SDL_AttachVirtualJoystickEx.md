###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AttachVirtualJoystickEx

Attach a new virtual joystick with extended properties.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickID SDL_AttachVirtualJoystickEx(const SDL_VirtualJoystickDesc *desc);

```

## Function Parameters

|              |                      |
| ------------ | -------------------- |
| **desc**     | Joystick description |

## Return Value

Returns the joystick instance ID, or 0 if an error occurred; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)
* [SDL_DetachVirtualJoystick](SDL_DetachVirtualJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

