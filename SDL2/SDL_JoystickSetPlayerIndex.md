###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickSetPlayerIndex

Set the player index of an opened joystick.

## Syntax

```c
void SDL_JoystickSetPlayerIndex(SDL_Joystick *joystick, int player_index);

```

## Function Parameters

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **joystick**         | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_JoystickOpen](SDL_JoystickOpen.md)()              |
| **player_index**     | Player index to assign to this joystick, or -1 to clear the player index and turn off player LEDs. |

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI.md)
