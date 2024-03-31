###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerFromInstanceID

Get the [SDL_GameController](SDL_GameController) associated with an instance id.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_GameController* SDL_GameControllerFromInstanceID(SDL_JoystickID joyid);

```

## Function Parameters

|               |                                                                         |
| ------------- | ----------------------------------------------------------------------- |
| **joyid**     | the instance id to get the [SDL_GameController](SDL_GameController) for |

## Return Value

Returns an [SDL_GameController](SDL_GameController) on success or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.4.

----
[CategoryAPI](CategoryAPI)

