###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadFromPlayerIndex

Get the [SDL_Gamepad](SDL_Gamepad) associated with a player index.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_Gamepad* SDL_GetGamepadFromPlayerIndex(int player_index);

```

## Function Parameters

|                      |                                                        |
| -------------------- | ------------------------------------------------------ |
| **player_index**     | the player index, which different from the instance ID |

## Return Value

Returns the [SDL_Gamepad](SDL_Gamepad) associated with a player index.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadPlayerIndex](SDL_GetGamepadPlayerIndex)
- [SDL_SetGamepadPlayerIndex](SDL_SetGamepadPlayerIndex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

