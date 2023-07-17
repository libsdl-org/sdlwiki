###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadStringForType

Convert from an [SDL_GamepadType](SDL_GamepadType) enum to a string.

## Syntax

```c
const char* SDL_GetGamepadStringForType(SDL_GamepadType type);

```

## Function Parameters

|              |                                                              |
| ------------ | ------------------------------------------------------------ |
| **type**     | an enum value for a given [SDL_GamepadType](SDL_GamepadType) |

## Return Value

Returns a string for the given type, or NULL if an invalid type is
specified. The string returned is of the format used by
[SDL_Gamepad](SDL_Gamepad) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free)() the returned string.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadTypeFromString](SDL_GetGamepadTypeFromString)

----
[CategoryAPI](CategoryAPI)

