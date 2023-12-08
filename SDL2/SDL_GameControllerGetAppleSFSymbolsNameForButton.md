###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetAppleSFSymbolsNameForButton

Return the sfSymbolsName for a given button on a game controller on Apple platforms.

## Syntax

```c
const char* SDL_GameControllerGetAppleSFSymbolsNameForButton(SDL_GameController *gamecontroller, SDL_GameControllerButton button);

```

## Function Parameters

|                        |                                 |
| ---------------------- | ------------------------------- |
| **gamecontroller**     | the controller to query         |
| **button**             | a button on the game controller |

## Return Value

Returns the sfSymbolsName or NULL if the name can't be found

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_GameControllerGetAppleSFSymbolsNameForAxis](SDL_GameControllerGetAppleSFSymbolsNameForAxis.md)

----
[CategoryAPI](CategoryAPI.md)
