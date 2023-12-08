###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetSerial

Get the serial number of an opened joystick, if available.

## Syntax

```c
const char * SDL_JoystickGetSerial(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)() |

## Return Value

Returns the serial number of the selected joystick, or NULL if unavailable.

## Remarks

Returns the serial number of the joystick, or NULL if it is not available.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
