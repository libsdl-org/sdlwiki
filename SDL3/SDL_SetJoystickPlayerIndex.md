# SDL_SetJoystickPlayerIndex

Set the player index of an opened joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SetJoystickPlayerIndex(SDL_Joystick *joystick, int player_index);
```

## Function Parameters

|                                |                  |                                                                                                    |
| ------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)().             |
| int                            | **player_index** | player index to assign to this joystick, or -1 to clear the player index and turn off player LEDs. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickPlayerIndex](SDL_GetJoystickPlayerIndex)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

