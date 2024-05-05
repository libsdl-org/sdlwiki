###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickFromPlayerIndex

Get the [SDL_Joystick](SDL_Joystick) associated with a player index.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_Joystick* SDL_GetJoystickFromPlayerIndex(int player_index);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **player_index**     | the player index to get the [SDL_Joystick](SDL_Joystick) for |

## Return Value

Returns an [SDL_Joystick](SDL_Joystick) on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickPlayerIndex](SDL_GetJoystickPlayerIndex)
- [SDL_SetJoystickPlayerIndex](SDL_SetJoystickPlayerIndex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

