###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetProduct

Get the USB product ID of an opened joystick, if available.

## Syntax

```c
Uint16 SDL_JoystickGetProduct(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)() |

## Return Value

Returns the USB product ID of the selected joystick, or 0 if unavailable.

## Remarks

If the product ID isn't available this function returns 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI.md)
