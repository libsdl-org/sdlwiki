###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetBall

Get the ball axis change since the last poll.

## Syntax

```c
int SDL_JoystickGetBall(SDL_Joystick *joystick,
                        int ball, int *dx, int *dy);

```

## Function Parameters

|                  |                                                                  |
| ---------------- | ---------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) to query                        |
| **ball**         | the ball index to query; ball indices start at index 0           |
| **dx**           | stores the difference in the x axis position since the last poll |
| **dy**           | stores the difference in the y axis position since the last poll |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Trackballs can only return relative motion since the last call to
[SDL_JoystickGetBall](SDL_JoystickGetBall.md)(), these motion deltas are
placed into `dx` and `dy`.

Most joysticks do not have trackballs.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickNumBalls](SDL_JoystickNumBalls.md)

----
[CategoryAPI](CategoryAPI.md)
