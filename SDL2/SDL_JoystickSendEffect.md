###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickSendEffect

Send a joystick specific effect packet

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickSendEffect(SDL_Joystick *joystick, const void *data, int size);
```

## Function Parameters

|                                |              |                                              |
| ------------------------------ | ------------ | -------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | The joystick to affect                       |
| const void *                   | **data**     | The data to send to the joystick             |
| int                            | **size**     | The size of the data to send to the joystick |

## Return Value

(int) Returns 0, or -1 if this joystick or driver doesn't support effect
packets

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

