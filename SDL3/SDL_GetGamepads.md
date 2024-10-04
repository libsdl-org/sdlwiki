###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGamepads

Get a list of currently connected gamepads.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_JoystickID * SDL_GetGamepads(int *count);
```

## Function Parameters

|       |           |                                                                        |
| ----- | --------- | ---------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of gamepads returned, may be NULL. |

## Return Value

([SDL_JoystickID](SDL_JoystickID) *) Returns a 0 terminated array of
joystick instance IDs or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HasGamepad](SDL_HasGamepad)
- [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

