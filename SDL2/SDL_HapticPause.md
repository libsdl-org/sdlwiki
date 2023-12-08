###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticPause

Pause a haptic device.

## Syntax

```c
int SDL_HapticPause(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to pause |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Device must support the [`SDL_HAPTIC_PAUSE`](SDL_HAPTIC_PAUSE) feature.
Call [SDL_HapticUnpause](SDL_HapticUnpause.md)() to resume playback.

Do not modify the effects nor add new ones while the device is paused. That
can cause all sorts of weird errors.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticUnpause](SDL_HapticUnpause.md)

----
[CategoryAPI](CategoryAPI.md)
