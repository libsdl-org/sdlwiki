###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetStringForAxis

Convert from an [SDL_GameControllerAxis](SDL_GameControllerAxis.md) enum to a string.

## Syntax

```c
const char* SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis axis);

```

## Function Parameters

|              |                                                                            |
| ------------ | -------------------------------------------------------------------------- |
| **axis**     | an enum value for a given [SDL_GameControllerAxis](SDL_GameControllerAxis.md) |

## Return Value

Returns a string for the given axis, or NULL if an invalid axis is
specified. The string returned is of the format used by
[SDL_GameController](SDL_GameController.md) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free.md)() the returned string.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerGetAxisFromString](SDL_GameControllerGetAxisFromString.md)

----
[CategoryAPI](CategoryAPI.md)
