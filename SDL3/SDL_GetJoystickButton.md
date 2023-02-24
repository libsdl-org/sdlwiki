###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickButton

Get the current state of a button on a joystick.

## Syntax

```c
Uint8 SDL_GetJoystickButton(SDL_Joystick *joystick,
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)

----
[CategoryAPI](CategoryAPI)

