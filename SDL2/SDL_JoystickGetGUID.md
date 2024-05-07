###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetGUID

Get the implementation-dependent GUID for the joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_JoystickOpen](SDL_JoystickOpen)() |

## Return Value

Returns the GUID of the given joystick. If called on an invalid index, this
function returns a zero GUID; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This function requires an open joystick.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_JoystickGetDeviceGUID](SDL_JoystickGetDeviceGUID)
- [SDL_JoystickGetGUIDString](SDL_JoystickGetGUIDString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

