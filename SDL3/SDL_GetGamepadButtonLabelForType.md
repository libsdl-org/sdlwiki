# SDL_GetGamepadButtonLabelForType

Get the label of a button on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadButtonLabel SDL_GetGamepadButtonLabelForType(SDL_GamepadType type, SDL_GamepadButton button);
```

## Function Parameters

|                                        |            |                                                                            |
| -------------------------------------- | ---------- | -------------------------------------------------------------------------- |
| [SDL_GamepadType](SDL_GamepadType)     | **type**   | the type of gamepad to check.                                              |
| [SDL_GamepadButton](SDL_GamepadButton) | **button** | a button index (one of the [SDL_GamepadButton](SDL_GamepadButton) values). |

## Return Value

([SDL_GamepadButtonLabel](SDL_GamepadButtonLabel)) Returns the
[SDL_GamepadButtonLabel](SDL_GamepadButtonLabel) enum corresponding to the
button label.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadButtonLabel](SDL_GetGamepadButtonLabel)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

