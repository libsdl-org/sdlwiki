# SDL_JoystickGetDeviceVendor

Get the USB vendor ID of a joystick, if available.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
Uint16 SDL_JoystickGetDeviceVendor(int device_index);
```

## Function Parameters

|     |                  |                                                                      |
| --- | ---------------- | -------------------------------------------------------------------- |
| int | **device_index** | the index of the joystick to query (the N'th joystick on the system. |

## Return Value

([Uint16](Uint16)) Returns the USB vendor ID of the selected joystick. If
called on an invalid index, this function returns zero.

## Remarks

This can be called before any joysticks are opened. If the vendor ID isn't
available this function returns 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

