###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGamepadPlayerIndex

Set the player index of an opened gamepad.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_SetGamepadPlayerIndex(SDL_Gamepad *gamepad, int player_index);

```

## Function Parameters

|                      |                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **gamepad**          | the gamepad object to adjust.                                                                     |
| **player_index**     | Player index to assign to this gamepad, or -1 to clear the player index and turn off player LEDs. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetGamepadPlayerIndex](SDL_GetGamepadPlayerIndex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

