###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerOpen

Open a game controller for use.

## Syntax

```c
SDL_GameController* SDL_GameControllerOpen(int joystick_index);

```

## Function Parameters

|                        |                                                                            |
| ---------------------- | -------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, up to [SDL_NumJoysticks](SDL_NumJoysticks.md)() |

## Return Value

Returns a gamecontroller identifier or NULL if an error occurred; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

`joystick_index` is the same as the `device_index` passed to
[SDL_JoystickOpen](SDL_JoystickOpen.md)().

The index passed as an argument refers to the N'th game controller on the
system. This index is not the value which will identify this controller in
future controller events. The joystick's instance id
([SDL_JoystickID](SDL_JoystickID.md)) will be used there instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerClose](SDL_GameControllerClose.md)
* [SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex.md)
* [SDL_IsGameController](SDL_IsGameController.md)

----
[CategoryAPI](CategoryAPI.md)
