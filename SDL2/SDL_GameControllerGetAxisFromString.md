###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetAxisFromString

Convert a string into [SDL_GameControllerAxis](SDL_GameControllerAxis) enum.

## Syntax

```c
SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(const char *str);

```

## Function Parameters

|             |                                                                     |
| ----------- | ------------------------------------------------------------------- |
| **str**     | string representing a [SDL_GameController](SDL_GameController) axis |

## Return Value

Returns the [SDL_GameControllerAxis](SDL_GameControllerAxis) enum
corresponding to the input string, or
`[SDL_CONTROLLER_AXIS_INVALID](SDL_CONTROLLER_AXIS_INVALID)` if no match
was found.

## Remarks

This function is called internally to translate
[SDL_GameController](SDL_GameController) mapping strings for the underlying
joystick device into the consistent
[SDL_GameController](SDL_GameController) mapping. You do not normally need
to call this function unless you are parsing
[SDL_GameController](SDL_GameController) mappings in your own code.

Note specially that "righttrigger" and "lefttrigger" map to
`[SDL_CONTROLLER_AXIS_TRIGGERRIGHT](SDL_CONTROLLER_AXIS_TRIGGERRIGHT)` and
`[SDL_CONTROLLER_AXIS_TRIGGERLEFT](SDL_CONTROLLER_AXIS_TRIGGERLEFT)`,
respectively.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerGetStringForAxis](SDL_GameControllerGetStringForAxis)

----
[CategoryAPI](CategoryAPI)

