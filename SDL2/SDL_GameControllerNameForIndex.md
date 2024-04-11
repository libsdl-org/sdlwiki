###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerNameForIndex

Get the implementation dependent name for the game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
const char* SDL_GameControllerNameForIndex(int joystick_index);

```

## Function Parameters

|                        |                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **joystick_index**     | the device_index of a device, from zero to [SDL_NumJoysticks](SDL_NumJoysticks)()-1 |

## Return Value

Returns the implementation-dependent name for the game controller, or NULL
if there is no name or the index is invalid.

## Remarks

This function can be called before any controllers are opened.

`joystick_index` is the same as the `device_index` passed to
[SDL_JoystickOpen](SDL_JoystickOpen)().

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GameControllerName](SDL_GameControllerName)
* [SDL_GameControllerOpen](SDL_GameControllerOpen)
* [SDL_IsGameController](SDL_IsGameController)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

