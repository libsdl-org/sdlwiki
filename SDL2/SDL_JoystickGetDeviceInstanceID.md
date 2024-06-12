###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDeviceInstanceID

Get the instance ID of a joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_JoystickID SDL_JoystickGetDeviceInstanceID(int device_index);
```

## Function Parameters

|     |                  |                                                                     |
| --- | ---------------- | ------------------------------------------------------------------- |
| int | **device_index** | the index of the joystick to query (the N'th joystick on the system |

## Return Value

([SDL_JoystickID](SDL_JoystickID)) Returns the instance id of the selected
joystick. If called on an invalid index, this function returns -1.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

