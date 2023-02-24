###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadButtonFromString

Convert a string into an [SDL_GamepadButton](SDL_GamepadButton) enum.

## Syntax

```c
SDL_GamepadButton SDL_GetGamepadButtonFromString(const char *str);

```

## Function Parameters

|             |                                                       |
| ----------- | ----------------------------------------------------- |
| **str**     | string representing a [SDL_Gamepad](SDL_Gamepad) axis |

## Return Value

Returns the [SDL_GamepadButton](SDL_GamepadButton) enum corresponding to
the input string, or [`SDL_GAMEPAD_AXIS_INVALID`](SDL_GAMEPAD_AXIS_INVALID)
if no match was found.

## Remarks

This function is called internally to translate [SDL_Gamepad](SDL_Gamepad)
mapping strings for the underlying joystick device into the consistent
[SDL_Gamepad](SDL_Gamepad) mapping. You do not normally need to call this
function unless you are parsing [SDL_Gamepad](SDL_Gamepad) mappings in your
own code.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

