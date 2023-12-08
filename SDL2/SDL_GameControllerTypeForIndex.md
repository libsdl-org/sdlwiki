###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerTypeForIndex

Get the type of a game controller.

## Syntax

```c
SDL_GameControllerType SDL_GameControllerTypeForIndex(int joystick_index);

```

## Function Parameters

|                        |                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, from zero to [SDL_NumJoysticks](SDL_NumJoysticks.md)()-1 |

## Return Value

Returns the controller type.

## Remarks

This can be called before any controllers are opened.

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI.md)
