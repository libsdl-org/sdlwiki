###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickFromPlayerIndex

Get the [SDL_Joystick](SDL_Joystick) associated with a player index.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_Joystick* SDL_JoystickFromPlayerIndex(int player_index);
```

## Function Parameters

|     |                  |                                                               |
| --- | ---------------- | ------------------------------------------------------------- |
| int | **player_index** | the player index to get the [SDL_Joystick](SDL_Joystick) for. |

## Return Value

([SDL_Joystick](SDL_Joystick) *) Returns an [SDL_Joystick](SDL_Joystick) on
success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

