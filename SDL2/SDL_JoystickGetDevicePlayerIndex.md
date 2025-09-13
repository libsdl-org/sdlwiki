# SDL_JoystickGetDevicePlayerIndex

Get the player index of a joystick, or -1 if it's not available This can be called before any joysticks are opened.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickGetDevicePlayerIndex(int device_index);
```

## Function Parameters

|     |                  |               |
| --- | ---------------- | ------------- |
| int | **device_index** | device index. |

## Return Value

(int) Returns player index, or -1 if not available.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

