###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadStringForButton

Convert from an [SDL_GamepadButton](SDL_GamepadButton) enum to a string.

## Syntax

```c
const char* SDL_GetGamepadStringForButton(SDL_GamepadButton button);

```

## Function Parameters

|                |                                                                  |
| -------------- | ---------------------------------------------------------------- |
| **button**     | an enum value for a given [SDL_GamepadButton](SDL_GamepadButton) |

## Return Value

Returns a string for the given button, or NULL if an invalid button is
specified. The string returned is of the format used by
[SDL_Gamepad](SDL_Gamepad) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free)() the returned string.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadButtonFromString](SDL_GetGamepadButtonFromString)

----
[CategoryAPI](CategoryAPI)

