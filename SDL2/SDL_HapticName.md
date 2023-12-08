###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticName

Get the implementation dependent name of a haptic device.

## Syntax

```c
const char* SDL_HapticName(int device_index);

```

## Function Parameters

|                      |                               |
| -------------------- | ----------------------------- |
| **device_index**     | index of the device to query. |

## Return Value

Returns the name of the device or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This can be called before any joysticks are opened. If no name can be
found, this function returns NULL.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_NumHaptics](SDL_NumHaptics.md)

----
[CategoryAPI](CategoryAPI.md)
