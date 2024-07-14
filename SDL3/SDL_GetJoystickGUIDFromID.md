###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickGUIDFromID

Get the implementation-dependent GUID of a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickGUID SDL_GetJoystickGUIDFromID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

([SDL_JoystickGUID](SDL_JoystickGUID)) Returns the GUID of the selected
joystick. If called with an invalid instance_id, this function returns a
zero GUID.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickGUID](SDL_GetJoystickGUID)
- [SDL_GetJoystickGUIDString](SDL_GetJoystickGUIDString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

