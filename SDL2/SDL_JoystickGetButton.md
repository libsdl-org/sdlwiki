###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetButton

Get the current state of a button on a joystick.

## Syntax

```c
Uint8 SDL_JoystickGetButton(SDL_Joystick *joystick,
                            int button);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |
| **button**       | the button index to get the state from; indices start at index 0          |

## Return Value

Returns 1 if the specified button is pressed, 0 otherwise.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickNumButtons](SDL_JoystickNumButtons)

----
[CategoryAPI](CategoryAPI)

