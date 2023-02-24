###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickHat

Get the current state of a POV hat on a joystick.

## Syntax

```c
Uint8 SDL_GetJoystickHat(SDL_Joystick *joystick,
                         int hat);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |
| **hat**          | the hat index to get the state from; indices start at index 0             |

## Return Value

Returns the current hat position.

## Remarks

The returned value will be one of the following positions:

- [`SDL_HAT_CENTERED`](SDL_HAT_CENTERED)
- [`SDL_HAT_UP`](SDL_HAT_UP)
- [`SDL_HAT_RIGHT`](SDL_HAT_RIGHT)
- [`SDL_HAT_DOWN`](SDL_HAT_DOWN)
- [`SDL_HAT_LEFT`](SDL_HAT_LEFT)
- [`SDL_HAT_RIGHTUP`](SDL_HAT_RIGHTUP)
- [`SDL_HAT_RIGHTDOWN`](SDL_HAT_RIGHTDOWN)
- [`SDL_HAT_LEFTUP`](SDL_HAT_LEFTUP)
- [`SDL_HAT_LEFTDOWN`](SDL_HAT_LEFTDOWN)

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumJoystickHats](SDL_GetNumJoystickHats)

----
[CategoryAPI](CategoryAPI)

