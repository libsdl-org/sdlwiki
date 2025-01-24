# SDL_GetJoystickPlayerIndexForID

Get the player index of a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_GetJoystickPlayerIndexForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

(int) Returns the player index of a joystick, or -1 if it's not available.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickPlayerIndex](SDL_GetJoystickPlayerIndex)
- [SDL_GetJoysticks](SDL_GetJoysticks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

