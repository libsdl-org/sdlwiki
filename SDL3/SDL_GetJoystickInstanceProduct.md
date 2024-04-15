###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickInstanceProduct

Get the USB product ID of a joystick, if available.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
Uint16 SDL_GetJoystickInstanceProduct(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the USB product ID of the selected joystick. If called with an
invalid instance_id, this function returns 0.

## Remarks

This can be called before any joysticks are opened. If the product ID isn't
available this function returns 0.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetJoystickProduct](SDL_GetJoystickProduct)
* [SDL_GetJoysticks](SDL_GetJoysticks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

