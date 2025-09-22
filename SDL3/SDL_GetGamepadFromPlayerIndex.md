# SDL_GetGamepadFromPlayerIndex

Get the [SDL_Gamepad](SDL_Gamepad) associated with a player index.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_Gamepad * SDL_GetGamepadFromPlayerIndex(int player_index);
```

## Function Parameters

|     |                  |                                                         |
| --- | ---------------- | ------------------------------------------------------- |
| int | **player_index** | the player index, which different from the instance ID. |

## Return Value

([SDL_Gamepad](SDL_Gamepad) *) Returns the [SDL_Gamepad](SDL_Gamepad)
associated with a player index.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadPlayerIndex](SDL_GetGamepadPlayerIndex)
- [SDL_SetGamepadPlayerIndex](SDL_SetGamepadPlayerIndex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

