###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_GameControllerGetStringForAxis

Convert from an [SDL_GameControllerAxis](SDL_GameControllerAxis) enum to a string.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
const char* SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis axis);
```

## Function Parameters

|                                                  |          |                                                                             |
| ------------------------------------------------ | -------- | --------------------------------------------------------------------------- |
| [SDL_GameControllerAxis](SDL_GameControllerAxis) | **axis** | an enum value for a given [SDL_GameControllerAxis](SDL_GameControllerAxis). |

## Return Value

(const char *) Returns a string for the given axis, or NULL if an invalid
axis is specified. The string returned is of the format used by
[SDL_GameController](SDL_GameController) mapping strings.

## Remarks

The caller should not [SDL_free](SDL_free)() the returned string.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerGetAxisFromString](SDL_GameControllerGetAxisFromString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

