###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDeviceProduct

Get the USB product ID of a joystick, if available.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Uint16 SDL_JoystickGetDeviceProduct(int device_index);

```

## Function Parameters

|                      |                                                                     |
| -------------------- | ------------------------------------------------------------------- |
| **device_index**     | the index of the joystick to query (the N'th joystick on the system |

## Return Value

Returns the USB product ID of the selected joystick. If called on an
invalid index, this function returns zero

## Remarks

This can be called before any joysticks are opened. If the product ID isn't
available this function returns 0.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

