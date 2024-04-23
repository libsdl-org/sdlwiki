###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetBindForAxis

Get the SDL joystick layer binding for a controller axis mapping.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
extern DECLSPEC SDL_GameControllerButtonBind SDLCALL
SDL_GameControllerGetBindForAxis(SDL_GameController *gamecontroller,
         SDL_GameControllerAxis axis);

```

## Function Parameters

|                        |                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **gamecontroller**     | a game controller                                                                       |
| **axis**               | an axis enum value (one of the [SDL_GameControllerAxis](SDL_GameControllerAxis) values) |

## Return Value

Returns a [SDL_GameControllerButtonBind](SDL_GameControllerButtonBind)
describing the bind. On failure (like the given Controller axis doesn't
exist on the device), its `.bindType` will be
[`SDL_CONTROLLER_BINDTYPE_NONE`](SDL_CONTROLLER_BINDTYPE_NONE).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerGetBindForButton](SDL_GameControllerGetBindForButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


