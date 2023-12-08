###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadButtonFromString

Convert a string into an [SDL_GamepadButton](SDL_GamepadButton.md) enum.

## Syntax

```c
SDL_GamepadButton SDL_GetGamepadButtonFromString(const char *str);

```

## Function Parameters

|             |                                                       |
| ----------- | ----------------------------------------------------- |
| **str**     | string representing a [SDL_Gamepad](SDL_Gamepad.md) axis |

## Return Value

Returns the [SDL_GamepadButton](SDL_GamepadButton.md) enum corresponding to
the input string, or
[`SDL_GAMEPAD_BUTTON_INVALID`](SDL_GAMEPAD_BUTTON_INVALID) if no match was
found.

## Remarks

This function is called internally to translate [SDL_Gamepad](SDL_Gamepad.md)
mapping strings for the underlying joystick device into the consistent
[SDL_Gamepad](SDL_Gamepad.md) mapping. You do not normally need to call this
function unless you are parsing [SDL_Gamepad](SDL_Gamepad.md) mappings in your
own code.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
