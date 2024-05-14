###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetBindForButton

Get the SDL joystick layer binding for a controller button mapping.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
extern DECLSPEC SDL_GameControllerButtonBind SDLCALL
SDL_GameControllerGetBindForButton(SDL_GameController *gamecontroller,
           SDL_GameControllerButton button);

```

## Function Parameters

|                        |                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **gamecontroller**     | a game controller                                                                    |
| **button**             | an button enum value (an [SDL_GameControllerButton](SDL_GameControllerButton) value) |

## Return Value

Returns a [SDL_GameControllerButtonBind](SDL_GameControllerButtonBind)
describing the bind. On failure (like the given Controller button doesn't
exist on the device), its `.bindType` will be
[`SDL_CONTROLLER_BINDTYPE_NONE`](SDL_CONTROLLER_BINDTYPE_NONE).

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerGetBindForAxis](SDL_GameControllerGetBindForAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

