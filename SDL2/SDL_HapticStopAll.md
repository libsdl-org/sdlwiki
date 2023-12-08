###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticStopAll

Stop all the currently playing effects on a haptic device.

## Syntax

```c
int SDL_HapticStopAll(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to stop |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
