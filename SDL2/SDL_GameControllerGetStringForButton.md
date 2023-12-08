###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetStringForButton

Convert from an [SDL_GameControllerButton](SDL_GameControllerButton.md) enum to a string.

## Syntax

```c
const char* SDL_GameControllerGetStringForButton(SDL_GameControllerButton button);

```

## Function Parameters

|                |                                                                                |
| -------------- | ------------------------------------------------------------------------------ |
| **button**     | an enum value for a given [SDL_GameControllerButton](SDL_GameControllerButton.md) |

## Return Value

Returns a string for the given button, or NULL if an invalid button is
specified. The string returned is of the format used by
[SDL_GameController](SDL_GameController.md) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free.md)() the returned string.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerGetButtonFromString](SDL_GameControllerGetButtonFromString.md)

----
[CategoryAPI](CategoryAPI.md)
