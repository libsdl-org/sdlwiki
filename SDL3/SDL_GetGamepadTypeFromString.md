# SDL_GetGamepadTypeFromString

Convert a string into [SDL_GamepadType](SDL_GamepadType) enum.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadType SDL_GetGamepadTypeFromString(const char *str);
```

## Function Parameters

|              |         |                                                                |
| ------------ | ------- | -------------------------------------------------------------- |
| const char * | **str** | string representing a [SDL_GamepadType](SDL_GamepadType) type. |

## Return Value

([SDL_GamepadType](SDL_GamepadType)) Returns the
[SDL_GamepadType](SDL_GamepadType) enum corresponding to the input string,
or [`SDL_GAMEPAD_TYPE_UNKNOWN`](SDL_GAMEPAD_TYPE_UNKNOWN) if no match was
found.

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

- [SDL_GetGamepadStringForType](SDL_GetGamepadStringForType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

