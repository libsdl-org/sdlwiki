###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticRumbleInit

Initialize a haptic device for simple rumble playback.

## Syntax

```c
int SDL_HapticRumbleInit(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                                            |
| -------------- | ---------------------------------------------------------- |
| **haptic**     | the haptic device to initialize for simple rumble playback |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpen](SDL_HapticOpen.md)
* [SDL_HapticRumblePlay](SDL_HapticRumblePlay.md)
* [SDL_HapticRumbleStop](SDL_HapticRumbleStop.md)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported.md)

----
[CategoryAPI](CategoryAPI.md)
