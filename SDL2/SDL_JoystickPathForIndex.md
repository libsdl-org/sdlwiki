###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickPathForIndex

Get the implementation dependent path of a joystick.

## Syntax

```c
const char* SDL_JoystickPathForIndex(int device_index);

```

## Function Parameters

|                      |                                                                      |
| -------------------- | -------------------------------------------------------------------- |
| **device_index**     | the index of the joystick to query (the N'th joystick on the system) |

## Return Value

Returns the path of the selected joystick. If no path can be found, this
function returns NULL; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_JoystickPath](SDL_JoystickPath.md)
* [SDL_JoystickOpen](SDL_JoystickOpen.md)

----
[CategoryAPI](CategoryAPI.md)
