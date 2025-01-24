# SDL_GetGamepadButton

Get the current state of a button on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GetGamepadButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
```

## Function Parameters

|                                        |             |                                                                            |
| -------------------------------------- | ----------- | -------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *           | **gamepad** | a gamepad.                                                                 |
| [SDL_GamepadButton](SDL_GamepadButton) | **button**  | a button index (one of the [SDL_GamepadButton](SDL_GamepadButton) values). |

## Return Value

(bool) Returns true if the button is pressed, false otherwise.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GamepadHasButton](SDL_GamepadHasButton)
- [SDL_GetGamepadAxis](SDL_GetGamepadAxis)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

