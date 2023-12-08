###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetProductVersion

Get the product version of an opened joystick, if available.

## Syntax

```c
Uint16 SDL_JoystickGetProductVersion(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)() |

## Return Value

Returns the product version of the selected joystick, or 0 if unavailable.

## Remarks

If the product version isn't available this function returns 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI.md)
