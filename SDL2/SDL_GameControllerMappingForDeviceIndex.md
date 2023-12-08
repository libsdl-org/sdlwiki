###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerMappingForDeviceIndex

Get the mapping of a game controller.

## Syntax

```c
char* SDL_GameControllerMappingForDeviceIndex(int joystick_index);

```

## Function Parameters

|                        |                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, from zero to [SDL_NumJoysticks](SDL_NumJoysticks.md)()-1 |

## Return Value

Returns the mapping string. Must be freed with [SDL_free](SDL_free.md)().
Returns NULL if no mapping is available.

## Remarks

This can be called before any controllers are opened.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
