# SDL_GamepadHasButton

Query whether a gamepad has a given button.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GamepadHasButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
```

## Function Parameters

|                                        |             |                                                                        |
| -------------------------------------- | ----------- | ---------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *           | **gamepad** | a gamepad.                                                             |
| [SDL_GamepadButton](SDL_GamepadButton) | **button**  | a button enum value (an [SDL_GamepadButton](SDL_GamepadButton) value). |

## Return Value

(bool) Returns true if the gamepad has this button, false otherwise.

## Remarks

This merely reports whether the gamepad's mapping defined this button, as
that is all the information SDL has about the physical device.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GamepadHasAxis](SDL_GamepadHasAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

