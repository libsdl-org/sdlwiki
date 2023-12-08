###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerPath

Get the implementation-dependent path for an opened game controller.

## Syntax

```c
const char* SDL_GameControllerPath(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **gamecontroller**     | a game controller identifier previously returned by [SDL_GameControllerOpen](SDL_GameControllerOpen.md)() |

## Return Value

Returns the implementation dependent path for the game controller, or NULL
if there is no path or the identifier passed is invalid.

## Remarks

This is the same path as returned by
[SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex.md)(), but it
takes a controller identifier instead of the (unstable) device index.

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_GameControllerPathForIndex](SDL_GameControllerPathForIndex.md)

----
[CategoryAPI](CategoryAPI.md)
