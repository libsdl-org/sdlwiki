###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticUnpause

Unpause a haptic device.

## Syntax

```c
int SDL_HapticUnpause(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to unpause |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Call to unpause after [SDL_HapticPause](SDL_HapticPause.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticPause](SDL_HapticPause.md)

----
[CategoryAPI](CategoryAPI.md)
