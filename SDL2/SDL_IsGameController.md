###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsGameController

Check if the given joystick is supported by the game controller interface.

## Syntax

```c
SDL_bool SDL_IsGameController(int joystick_index);

```

## Function Parameters

|                        |                                                                            |
| ---------------------- | -------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, up to [SDL_NumJoysticks](SDL_NumJoysticks.md)() |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the given joystick is supported by the game
controller interface, [SDL_FALSE](SDL_FALSE.md) if it isn't or it's an invalid
index.

## Remarks

`joystick_index` is the same as the `device_index` passed to
[SDL_JoystickOpen](SDL_JoystickOpen.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex.md)
* [SDL_GameControllerOpen](SDL_GameControllerOpen.md)

----
[CategoryAPI](CategoryAPI.md)
