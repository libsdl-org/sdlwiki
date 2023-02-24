###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickNumButtons

Get the number of buttons on a joystick.

## Syntax

```c
int SDL_JoystickNumButtons(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |

## Return Value

Returns the number of buttons on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetButton](SDL_JoystickGetButton)
* [SDL_JoystickOpen](SDL_JoystickOpen)

----
[CategoryAPI](CategoryAPI)

