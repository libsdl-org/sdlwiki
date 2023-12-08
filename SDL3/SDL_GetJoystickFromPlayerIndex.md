###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickFromPlayerIndex

Get the [SDL_Joystick](SDL_Joystick.md) associated with a player index.

## Syntax

```c
SDL_Joystick* SDL_GetJoystickFromPlayerIndex(int player_index);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **player_index**     | the player index to get the [SDL_Joystick](SDL_Joystick.md) for |

## Return Value

Returns an [SDL_Joystick](SDL_Joystick.md) on success or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
