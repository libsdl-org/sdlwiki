# SDL_GetJoystickGUID

Get the implementation-dependent GUID for the joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_GUID SDL_GetJoystickGUID(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                                        |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)(). |

## Return Value

([SDL_GUID](SDL_GUID)) Returns the GUID of the given joystick. If called on
an invalid index, this function returns a zero GUID; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function requires an open joystick.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickGUIDForID](SDL_GetJoystickGUIDForID)
- [SDL_GUIDToString](SDL_GUIDToString)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

