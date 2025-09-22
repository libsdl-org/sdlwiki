# SDL_GetJoystickBall

Get the ball axis change since the last poll.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_GetJoystickBall(SDL_Joystick *joystick, int ball, int *dx, int *dy);
```

## Function Parameters

|                                |              |                                                                   |
| ------------------------------ | ------------ | ----------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) to query.                        |
| int                            | **ball**     | the ball index to query; ball indices start at index 0.           |
| int *                          | **dx**       | stores the difference in the x axis position since the last poll. |
| int *                          | **dy**       | stores the difference in the y axis position since the last poll. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Trackballs can only return relative motion since the last call to
[SDL_GetJoystickBall](SDL_GetJoystickBall)(), these motion deltas are
placed into `dx` and `dy`.

Most joysticks do not have trackballs.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumJoystickBalls](SDL_GetNumJoystickBalls)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

