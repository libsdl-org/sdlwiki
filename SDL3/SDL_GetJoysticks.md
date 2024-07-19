###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoysticks

Get a list of currently connected joysticks.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
const SDL_JoystickID * SDL_GetJoysticks(int *count);
```

## Function Parameters

|       |           |                                                                         |
| ----- | --------- | ----------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of joysticks returned, may be NULL. |

## Return Value

(const [SDL_JoystickID](SDL_JoystickID) *) Returns a 0 terminated array of
joystick instance IDs or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HasJoystick](SDL_HasJoystick)
- [SDL_OpenJoystick](SDL_OpenJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

