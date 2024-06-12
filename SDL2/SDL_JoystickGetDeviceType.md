###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDeviceType

Get the type of a joystick, if available.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_JoystickType SDL_JoystickGetDeviceType(int device_index);
```

## Function Parameters

|     |                  |                                                                     |
| --- | ---------------- | ------------------------------------------------------------------- |
| int | **device_index** | the index of the joystick to query (the N'th joystick on the system |

## Return Value

([SDL_JoystickType](SDL_JoystickType)) Returns the
[SDL_JoystickType](SDL_JoystickType) of the selected joystick. If called on
an invalid index, this function returns
[`SDL_JOYSTICK_TYPE_UNKNOWN`](SDL_JOYSTICK_TYPE_UNKNOWN)

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

