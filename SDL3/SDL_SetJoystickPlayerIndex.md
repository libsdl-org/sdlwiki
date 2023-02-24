###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickPlayerIndex

Set the player index of an opened joystick.

## Syntax

```c
int SDL_SetJoystickPlayerIndex(SDL_Joystick *joystick, int player_index);

```

## Function Parameters

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **joystick**         | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)()              |
| **player_index**     | Player index to assign to this joystick, or -1 to clear the player index and turn off player LEDs. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

