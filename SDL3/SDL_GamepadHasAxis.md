# SDL_GamepadHasAxis

Query whether a gamepad has a given axis.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GamepadHasAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
```

## Function Parameters

|                                    |             |                                                                   |
| ---------------------------------- | ----------- | ----------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *       | **gamepad** | a gamepad.                                                        |
| [SDL_GamepadAxis](SDL_GamepadAxis) | **axis**    | an axis enum value (an [SDL_GamepadAxis](SDL_GamepadAxis) value). |

## Return Value

(bool) Returns true if the gamepad has this axis, false otherwise.

## Remarks

This merely reports whether the gamepad's mapping defined this axis, as
that is all the information SDL has about the physical device.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GamepadHasButton](SDL_GamepadHasButton)
- [SDL_GetGamepadAxis](SDL_GetGamepadAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

