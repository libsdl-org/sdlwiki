###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadAppleSFSymbolsNameForAxis

Return the sfSymbolsName for a given axis on a gamepad on Apple platforms.

## Syntax

```c
const char* SDL_GetGamepadAppleSFSymbolsNameForAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);

```

## Function Parameters

|                 |                        |
| --------------- | ---------------------- |
| **gamepad**     | the gamepad to query   |
| **axis**        | an axis on the gamepad |

## Return Value

Returns the sfSymbolsName or NULL if the name can't be found

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadAppleSFSymbolsNameForButton](SDL_GetGamepadAppleSFSymbolsNameForButton)

----
[CategoryAPI](CategoryAPI)

