###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerEventState

Query or change current state of Game Controller events.

## Syntax

```c
int SDL_GameControllerEventState(int state);

```

## Function Parameters

|               |                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------- |
| **state**     | can be one of `[SDL_QUERY](SDL_QUERY)`, `[SDL_IGNORE](SDL_IGNORE)`, or `[SDL_ENABLE](SDL_ENABLE)` |

## Return Value

Returns the same value passed to the function, with exception to -1
([SDL_QUERY](SDL_QUERY)), which will return the current state.

## Remarks

If controller events are disabled, you must call
[SDL_GameControllerUpdate](SDL_GameControllerUpdate)() yourself and check
the state of the controller when you want controller information.

Any number can be passed to
[SDL_GameControllerEventState](SDL_GameControllerEventState)(), but only
-1, 0, and 1 will have any effect. Other numbers will just be returned.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickEventState](SDL_JoystickEventState)

----
[CategoryAPI](CategoryAPI)

