###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickDetachVirtual

Detach a virtual joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickDetachVirtual(int device_index);

```

## Function Parameters

|                      |                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **device_index**     | a value previously returned from [SDL_JoystickAttachVirtual](SDL_JoystickAttachVirtual)() |

## Return Value

Returns 0 on success, or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

