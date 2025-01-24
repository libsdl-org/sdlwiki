# SDL_JoystickGetVendor

Get the USB vendor ID of an opened joystick, if available.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
Uint16 SDL_JoystickGetVendor(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                                        |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_JoystickOpen](SDL_JoystickOpen)(). |

## Return Value

([Uint16](Uint16)) Returns the USB vendor ID of the selected joystick, or 0
if unavailable.

## Remarks

If the vendor ID isn't available this function returns 0.

## Version

This function is available since SDL 2.0.6.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

