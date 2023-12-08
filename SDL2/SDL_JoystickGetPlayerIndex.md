###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetPlayerIndex

Get the player index of an opened joystick.

## Syntax

```c
int SDL_JoystickGetPlayerIndex(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)() |

## Return Value

Returns the player index, or -1 if it's not available.

## Remarks

For XInput controllers this returns the XInput user index. Many joysticks
will not be able to supply this information.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
