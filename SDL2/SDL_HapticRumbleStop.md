###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticRumbleStop

Stop the simple rumble on a haptic device.

## Syntax

```c
int SDL_HapticRumbleStop(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **haptic**     | the haptic device to stop the rumble effect on |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticRumbleInit](SDL_HapticRumbleInit)
* [SDL_HapticRumblePlay](SDL_HapticRumblePlay)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)

----
[CategoryAPI](CategoryAPI)

