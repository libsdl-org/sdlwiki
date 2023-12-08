###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticIndex

Get the index of a haptic device.

## Syntax

```c
int SDL_HapticIndex(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |

## Return Value

Returns the index of the specified haptic device or a negative error code
on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpen](SDL_HapticOpen.md)
* [SDL_HapticOpened](SDL_HapticOpened.md)

----
[CategoryAPI](CategoryAPI.md)
