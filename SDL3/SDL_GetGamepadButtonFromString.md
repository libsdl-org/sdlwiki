# SDL_GetGamepadButtonFromString

Convert a string into an [SDL_GamepadButton](SDL_GamepadButton) enum.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadButton SDL_GetGamepadButtonFromString(const char *str);
```

## Function Parameters

|              |         |                                                        |
| ------------ | ------- | ------------------------------------------------------ |
| const char * | **str** | string representing a [SDL_Gamepad](SDL_Gamepad) axis. |

## Return Value

([SDL_GamepadButton](SDL_GamepadButton)) Returns the
[SDL_GamepadButton](SDL_GamepadButton) enum corresponding to the input
string, or [`SDL_GAMEPAD_BUTTON_INVALID`](SDL_GAMEPAD_BUTTON_INVALID) if no
match was found.

## Remarks

This function is called internally to translate [SDL_Gamepad](SDL_Gamepad)
mapping strings for the underlying joystick device into the consistent
[SDL_Gamepad](SDL_Gamepad) mapping. You do not normally need to call this
function unless you are parsing [SDL_Gamepad](SDL_Gamepad) mappings in your
own code.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadStringForButton](SDL_GetGamepadStringForButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

