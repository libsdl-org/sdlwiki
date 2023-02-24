###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadAxisFromString

Convert a string into [SDL_GamepadAxis](SDL_GamepadAxis) enum.

## Syntax

```c
SDL_GamepadAxis SDL_GetGamepadAxisFromString(const char *str);

```

## Function Parameters

|             |                                                       |
| ----------- | ----------------------------------------------------- |
| **str**     | string representing a [SDL_Gamepad](SDL_Gamepad) axis |

## Return Value

Returns the [SDL_GamepadAxis](SDL_GamepadAxis) enum corresponding to the
input string, or [`SDL_GAMEPAD_AXIS_INVALID`](SDL_GAMEPAD_AXIS_INVALID) if
no match was found.

## Remarks

This function is called internally to translate [SDL_Gamepad](SDL_Gamepad)
mapping strings for the underlying joystick device into the consistent
[SDL_Gamepad](SDL_Gamepad) mapping. You do not normally need to call this
function unless you are parsing [SDL_Gamepad](SDL_Gamepad) mappings in your
own code.

Note specially that "righttrigger" and "lefttrigger" map to
[`SDL_GAMEPAD_AXIS_RIGHT_TRIGGER`](SDL_GAMEPAD_AXIS_RIGHT_TRIGGER) and
[`SDL_GAMEPAD_AXIS_LEFT_TRIGGER`](SDL_GAMEPAD_AXIS_LEFT_TRIGGER),
respectively.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadStringForAxis](SDL_GetGamepadStringForAxis)

----
[CategoryAPI](CategoryAPI)

