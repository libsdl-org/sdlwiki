###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasButton

Query whether a game controller has a given button.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
SDL_bool SDL_GameControllerHasButton(SDL_GameController *gamecontroller,
                                     SDL_GameControllerButton button);

```

## Function Parameters

|                        |                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **gamecontroller**     | a game controller                                                                   |
| **button**             | a button enum value (an [SDL_GameControllerButton](SDL_GameControllerButton) value) |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the controller has this button,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This merely reports whether the controller's mapping defined this button,
as that is all the information SDL has about the physical device.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

