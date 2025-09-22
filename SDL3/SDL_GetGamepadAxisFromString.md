# SDL_GetGamepadAxisFromString

Convert a string into [SDL_GamepadAxis](SDL_GamepadAxis) enum.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadAxis SDL_GetGamepadAxisFromString(const char *str);
```

## Function Parameters

|              |         |                                                        |
| ------------ | ------- | ------------------------------------------------------ |
| const char * | **str** | string representing a [SDL_Gamepad](SDL_Gamepad) axis. |

## Return Value

([SDL_GamepadAxis](SDL_GamepadAxis)) Returns the
[SDL_GamepadAxis](SDL_GamepadAxis) enum corresponding to the input string,
or [`SDL_GAMEPAD_AXIS_INVALID`](SDL_GAMEPAD_AXIS_INVALID) if no match was
found.

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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadStringForAxis](SDL_GetGamepadStringForAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

