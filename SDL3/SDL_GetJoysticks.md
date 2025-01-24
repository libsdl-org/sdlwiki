# SDL_GetJoysticks

Get a list of currently connected joysticks.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickID * SDL_GetJoysticks(int *count);
```

## Function Parameters

|       |           |                                                                         |
| ----- | --------- | ----------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of joysticks returned, may be NULL. |

## Return Value

([SDL_JoystickID](SDL_JoystickID) *) Returns a 0 terminated array of
joystick instance IDs or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_HasJoystick](SDL_HasJoystick)
- [SDL_OpenJoystick](SDL_OpenJoystick)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

