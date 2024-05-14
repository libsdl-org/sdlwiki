###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSendEffect

Send a controller specific effect packet

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerSendEffect(SDL_GameController *gamecontroller, const void *data, int size);

```

## Function Parameters

|                        |                                                |
| ---------------------- | ---------------------------------------------- |
| **gamecontroller**     | The controller to affect                       |
| **data**               | The data to send to the controller             |
| **size**               | The size of the data to send to the controller |

## Return Value

Returns 0, or -1 if this controller or driver doesn't support effect
packets

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

