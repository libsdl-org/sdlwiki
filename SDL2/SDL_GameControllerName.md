###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerName

Get the implementation-dependent name for an opened game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
const char* SDL_GameControllerName(SDL_GameController *gamecontroller);
```

## Function Parameters

|                                            |                    |                                                                                                         |
| ------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | a game controller identifier previously returned by [SDL_GameControllerOpen](SDL_GameControllerOpen)(). |

## Return Value

(const char *) Returns the implementation dependent name for the game
controller, or NULL if there is no name or the identifier passed is
invalid.

## Remarks

This is the same name as returned by
[SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex)(), but it
takes a controller identifier instead of the (unstable) device index.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex)
- [SDL_GameControllerOpen](SDL_GameControllerOpen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

