# SDL_GetJoystickGUIDForID

Get the implementation-dependent GUID of a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_GUID SDL_GetJoystickGUIDForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

([SDL_GUID](SDL_GUID)) Returns the GUID of the selected joystick. If called
with an invalid instance_id, this function returns a zero GUID.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickGUID](SDL_GetJoystickGUID)
- [SDL_GUIDToString](SDL_GUIDToString)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

