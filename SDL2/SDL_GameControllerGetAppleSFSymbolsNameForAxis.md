###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetAppleSFSymbolsNameForAxis

Return the sfSymbolsName for a given axis on a game controller on Apple platforms.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
const char* SDL_GameControllerGetAppleSFSymbolsNameForAxis(SDL_GameController *gamecontroller, SDL_GameControllerAxis axis);

```

## Function Parameters

|                        |                                |
| ---------------------- | ------------------------------ |
| **gamecontroller**     | the controller to query        |
| **axis**               | an axis on the game controller |

## Return Value

Returns the sfSymbolsName or NULL if the name can't be found

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_GameControllerGetAppleSFSymbolsNameForButton](SDL_GameControllerGetAppleSFSymbolsNameForButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

