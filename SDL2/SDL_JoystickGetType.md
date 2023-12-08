###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetType

Get the type of an opened joystick.

## Syntax

```c
SDL_JoystickType SDL_JoystickGetType(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)() |

## Return Value

Returns the [SDL_JoystickType](SDL_JoystickType.md) of the selected joystick.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI.md)
