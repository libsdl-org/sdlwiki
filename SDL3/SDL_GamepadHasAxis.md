###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadHasAxis

Query whether a gamepad has a given axis.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_bool SDL_GamepadHasAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);

```

## Function Parameters

|                 |                                                                  |
| --------------- | ---------------------------------------------------------------- |
| **gamepad**     | a gamepad                                                        |
| **axis**        | an axis enum value (an [SDL_GamepadAxis](SDL_GamepadAxis) value) |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the gamepad has this axis,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This merely reports whether the gamepad's mapping defined this axis, as
that is all the information SDL has about the physical device.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GamepadHasButton](SDL_GamepadHasButton)
- [SDL_GetGamepadAxis](SDL_GetGamepadAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

