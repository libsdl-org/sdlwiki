###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetAxis

Get the current state of an axis control on a game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
extern DECLSPEC Sint16 SDLCALL
SDL_GameControllerGetAxis(SDL_GameController *gamecontroller, SDL_GameControllerAxis axis);

```

## Function Parameters

|                        |                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **gamecontroller**     | a game controller                                                                  |
| **axis**               | an axis index (one of the [SDL_GameControllerAxis](SDL_GameControllerAxis) values) |

## Return Value

Returns axis state (including 0) on success or 0 (also) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The axis indices start at index 0.

For thumbsticks, the state is a value ranging from -32768 (up/left) to
32767 (down/right).

Triggers range from 0 when released to 32767 when fully pressed, and never
return a negative value. Note that this differs from the value reported by
the lower-level [SDL_GetJoystickAxis](SDL_GetJoystickAxis)(), which
normally uses the full range.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerGetButton](SDL_GameControllerGetButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

