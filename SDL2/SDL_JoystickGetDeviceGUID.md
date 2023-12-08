###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDeviceGUID

Get the implementation-dependent GUID for the joystick at a given device index.

## Syntax

```c
SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int device_index);

```

## Function Parameters

|                      |                                                                     |
| -------------------- | ------------------------------------------------------------------- |
| **device_index**     | the index of the joystick to query (the N'th joystick on the system |

## Return Value

Returns the GUID of the selected joystick. If called on an invalid index,
this function returns a zero GUID

## Remarks

This function can be called before any joysticks are opened.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetGUID](SDL_JoystickGetGUID.md)
* [SDL_JoystickGetGUIDString](SDL_JoystickGetGUIDString.md)

----
[CategoryAPI](CategoryAPI.md)
