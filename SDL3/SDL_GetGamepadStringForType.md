###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGamepadStringForType

Convert from an [SDL_GamepadType](SDL_GamepadType) enum to a string.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadStringForType(SDL_GamepadType type);
```

## Function Parameters

|                                    |          |                                                               |
| ---------------------------------- | -------- | ------------------------------------------------------------- |
| [SDL_GamepadType](SDL_GamepadType) | **type** | an enum value for a given [SDL_GamepadType](SDL_GamepadType). |

## Return Value

(const char *) Returns a string for the given type, or NULL if an invalid
type is specified. The string returned is of the format used by
[SDL_Gamepad](SDL_Gamepad) mapping strings.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadTypeFromString](SDL_GetGamepadTypeFromString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

