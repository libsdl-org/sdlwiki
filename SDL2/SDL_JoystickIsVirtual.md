###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickIsVirtual

Query whether or not the joystick at a given device index is virtual.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_JoystickIsVirtual(int device_index);

```

## Function Parameters

|                      |                          |
| -------------------- | ------------------------ |
| **device_index**     | a joystick device index. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the joystick is virtual,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

