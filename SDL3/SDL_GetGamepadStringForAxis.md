###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadStringForAxis

Convert from an [SDL_GamepadAxis](SDL_GamepadAxis) enum to a string.

## Syntax

```c
const char* SDL_GetGamepadStringForAxis(SDL_GamepadAxis axis);

```

## Function Parameters

|              |                                                              |
| ------------ | ------------------------------------------------------------ |
| **axis**     | an enum value for a given [SDL_GamepadAxis](SDL_GamepadAxis) |

## Return Value

Returns a string for the given axis, or NULL if an invalid axis is
specified. The string returned is of the format used by
[SDL_Gamepad](SDL_Gamepad) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free)() the returned string.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadAxisFromString](SDL_GetGamepadAxisFromString)

----
[CategoryAPI](CategoryAPI)

