###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerPathForIndex

Get the implementation dependent path for the game controller.

## Syntax

```c
const char* SDL_GameControllerPathForIndex(int joystick_index);

```

## Function Parameters

|                        |                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, from zero to [SDL_NumJoysticks](SDL_NumJoysticks)()-1 |

## Return Value

Returns the implementation-dependent path for the game controller, or NULL
if there is no path or the index is invalid.

## Remarks

This function can be called before any controllers are opened.

`joystick_index` is the same as the `device_index` passed to
[SDL_JoystickOpen](SDL_JoystickOpen)().

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_GameControllerPath](SDL_GameControllerPath)

----
[CategoryAPI](CategoryAPI)

