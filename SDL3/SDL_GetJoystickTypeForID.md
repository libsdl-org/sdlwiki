# SDL_GetJoystickTypeForID

Get the type of a joystick, if available.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickType SDL_GetJoystickTypeForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

([SDL_JoystickType](SDL_JoystickType)) Returns the
[SDL_JoystickType](SDL_JoystickType) of the selected joystick. If called
with an invalid instance_id, this function returns
[`SDL_JOYSTICK_TYPE_UNKNOWN`](SDL_JOYSTICK_TYPE_UNKNOWN).

## Remarks

This can be called before any joysticks are opened.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickType](SDL_GetJoystickType)
- [SDL_GetJoysticks](SDL_GetJoysticks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

