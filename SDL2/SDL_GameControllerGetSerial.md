###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetSerial

Get the serial number of an opened controller, if available.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
const char * SDL_GameControllerGetSerial(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                      |
| ---------------------- | ------------------------------------ |
| **gamecontroller**     | the game controller object to query. |

## Return Value

Return the serial number, or NULL if unavailable.

## Remarks

Returns the serial number of the controller, or NULL if it is not
available.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

