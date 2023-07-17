###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadTypeFromString

Convert a string into [SDL_GamepadType](SDL_GamepadType) enum.

## Syntax

```c
SDL_GamepadType SDL_GetGamepadTypeFromString(const char *str);

```

## Function Parameters

|             |                                                               |
| ----------- | ------------------------------------------------------------- |
| **str**     | string representing a [SDL_GamepadType](SDL_GamepadType) type |

## Return Value

Returns the [SDL_GamepadType](SDL_GamepadType) enum corresponding to the
input string, or [`SDL_GAMEPAD_TYPE_UNKNOWN`](SDL_GAMEPAD_TYPE_UNKNOWN) if
no match was found.

## Remarks

This function is called internally to translate [SDL_Gamepad](SDL_Gamepad)
mapping strings for the underlying joystick device into the consistent
[SDL_Gamepad](SDL_Gamepad) mapping. You do not normally need to call this
function unless you are parsing [SDL_Gamepad](SDL_Gamepad) mappings in your
own code.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadStringForType](SDL_GetGamepadStringForType)

----
[CategoryAPI](CategoryAPI)

