###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickSetPlayerIndex

Set the player index of an opened joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
void SDL_JoystickSetPlayerIndex(SDL_Joystick *joystick, int player_index);
```

## Function Parameters

|                                |                  |                                                                                                    |
| ------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_JoystickOpen](SDL_JoystickOpen)()              |
| int                            | **player_index** | Player index to assign to this joystick, or -1 to clear the player index and turn off player LEDs. |

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

