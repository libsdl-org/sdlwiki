###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadAxis

Get the current state of an axis control on a gamepad.

## Syntax

```c
Sint16 SDL_GetGamepadAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);

```

## Function Parameters

|                 |                                                                      |
| --------------- | -------------------------------------------------------------------- |
| **gamepad**     | a gamepad                                                            |
| **axis**        | an axis index (one of the [SDL_GamepadAxis](SDL_GamepadAxis) values) |

## Return Value

Returns axis state (including 0) on success or 0 (also) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The axis indices start at index 0.

The state is a value ranging from -32768 to 32767. Triggers, however, range
from 0 to 32767 (they never return a negative value).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadButton](SDL_GetGamepadButton)

----
[CategoryAPI](CategoryAPI)

