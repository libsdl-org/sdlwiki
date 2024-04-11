###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetPlayerIndex

Get the player index of an opened game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_GameControllerGetPlayerIndex(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                      |
| ---------------------- | ------------------------------------ |
| **gamecontroller**     | the game controller object to query. |

## Return Value

Returns the player index for controller, or -1 if it's not available.

## Remarks

For XInput controllers this returns the XInput user index.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

