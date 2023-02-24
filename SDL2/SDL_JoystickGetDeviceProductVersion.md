###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDeviceProductVersion

Get the product version of a joystick, if available.

## Syntax

```c
Uint16 SDL_JoystickGetDeviceProductVersion(int device_index);

```

## Function Parameters

|                      |                                                                     |
| -------------------- | ------------------------------------------------------------------- |
| **device_index**     | the index of the joystick to query (the N'th joystick on the system |

## Return Value

Returns the product version of the selected joystick. If called on an
invalid index, this function returns zero

## Remarks

This can be called before any joysticks are opened. If the product version
isn't available this function returns 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI)

