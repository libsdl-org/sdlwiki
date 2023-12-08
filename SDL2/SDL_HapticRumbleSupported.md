###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticRumbleSupported

Check whether rumble is supported on a haptic device.

## Syntax

```c
int SDL_HapticRumbleSupported(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                           |
| -------------- | ----------------------------------------- |
| **haptic**     | haptic device to check for rumble support |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if effect is supported, [SDL_FALSE](SDL_FALSE.md)
if it isn't, or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticRumbleInit](SDL_HapticRumbleInit.md)
* [SDL_HapticRumblePlay](SDL_HapticRumblePlay.md)
* [SDL_HapticRumbleStop](SDL_HapticRumbleStop.md)

----
[CategoryAPI](CategoryAPI.md)
