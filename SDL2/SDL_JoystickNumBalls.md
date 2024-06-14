###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickNumBalls

Get the number of trackballs on a joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickNumBalls(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                            |
| ------------------------------ | ------------ | -------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | an [SDL_Joystick](SDL_Joystick) structure containing joystick information. |

## Return Value

(int) Returns the number of trackballs on success or a negative error code
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Joystick trackballs have only relative motion events associated with them
and their state cannot be polled.

Most joysticks do not have trackballs.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_JoystickGetBall](SDL_JoystickGetBall)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

