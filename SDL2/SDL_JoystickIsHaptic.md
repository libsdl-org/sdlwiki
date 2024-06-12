###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickIsHaptic

Query if a joystick has haptic features.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_JoystickIsHaptic(SDL_Joystick * joystick);
```

## Function Parameters

|                                |              |                                                                  |
| ------------------------------ | ------------ | ---------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) to test for haptic capabilities |

## Return Value

(int) Returns [SDL_TRUE](SDL_TRUE) if the joystick is haptic,
[SDL_FALSE](SDL_FALSE) if it isn't, or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_HapticOpenFromJoystick](SDL_HapticOpenFromJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

