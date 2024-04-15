###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadAppleSFSymbolsNameForButton

Return the sfSymbolsName for a given button on a gamepad on Apple platforms.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const char* SDL_GetGamepadAppleSFSymbolsNameForButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);

```

## Function Parameters

|                 |                         |
| --------------- | ----------------------- |
| **gamepad**     | the gamepad to query    |
| **button**      | a button on the gamepad |

## Return Value

Returns the sfSymbolsName or NULL if the name can't be found

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetGamepadAppleSFSymbolsNameForAxis](SDL_GetGamepadAppleSFSymbolsNameForAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

