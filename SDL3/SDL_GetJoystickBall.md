###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickBall

Get the ball axis change since the last poll.

## Syntax

```c
int SDL_GetJoystickBall(SDL_Joystick *joystick, int ball, int *dx, int *dy);

```

## Function Parameters

|                  |                                                                  |
| ---------------- | ---------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to query                        |
| **ball**         | the ball index to query; ball indices start at index 0           |
| **dx**           | stores the difference in the x axis position since the last poll |
| **dy**           | stores the difference in the y axis position since the last poll |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Trackballs can only return relative motion since the last call to
[SDL_GetJoystickBall](SDL_GetJoystickBall)(), these motion deltas are
placed into `dx` and `dy`.

Most joysticks do not have trackballs.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)

----
[CategoryAPI](CategoryAPI)

