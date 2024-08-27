###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickBall

Get the ball axis change since the last poll.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_GetJoystickBall(SDL_Joystick *joystick, int ball, int *dx, int *dy);
```

## Function Parameters

|                                |              |                                                                   |
| ------------------------------ | ------------ | ----------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) to query.                        |
| int                            | **ball**     | the ball index to query; ball indices start at index 0.           |
| int *                          | **dx**       | stores the difference in the x axis position since the last poll. |
| int *                          | **dy**       | stores the difference in the y axis position since the last poll. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Trackballs can only return relative motion since the last call to
[SDL_GetJoystickBall](SDL_GetJoystickBall)(), these motion deltas are
placed into `dx` and `dy`.

Most joysticks do not have trackballs.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

