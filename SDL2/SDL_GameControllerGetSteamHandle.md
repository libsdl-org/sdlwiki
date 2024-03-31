###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetSteamHandle

Get the Steam Input handle of an opened controller, if available.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Uint64 SDL_GameControllerGetSteamHandle(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                      |
| ---------------------- | ------------------------------------ |
| **gamecontroller**     | the game controller object to query. |

## Return Value

Returns the gamepad handle, or 0 if unavailable.

## Remarks

Returns an InputHandle_t for the controller that can be used with Steam
Input API: https://partner.steamgames.com/doc/api/ISteamInput

## Version

This function is available since SDL 2.30.0.

----
[CategoryAPI](CategoryAPI)

