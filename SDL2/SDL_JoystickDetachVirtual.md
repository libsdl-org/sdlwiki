# SDL_JoystickDetachVirtual

Detach a virtual joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickDetachVirtual(int device_index);
```

## Function Parameters

|     |                  |                                                                                            |
| --- | ---------------- | ------------------------------------------------------------------------------------------ |
| int | **device_index** | a value previously returned from [SDL_JoystickAttachVirtual](SDL_JoystickAttachVirtual)(). |

## Return Value

(int) Returns 0 on success, or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

