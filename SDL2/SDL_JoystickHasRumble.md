###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickHasRumble

Query whether a joystick has rumble support.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_bool SDL_JoystickHasRumble(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                       |
| ------------------------------ | ------------ | --------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | The joystick to query |

## Return Value

([SDL_bool](SDL_bool)) Return [SDL_TRUE](SDL_TRUE) if the joystick has
rumble, [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_JoystickRumble](SDL_JoystickRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

