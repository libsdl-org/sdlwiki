###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticRumblePlay

Run a simple rumble effect on a haptic device.

## Syntax

```c
int SDL_HapticRumblePlay(SDL_Haptic * haptic, float strength, Uint32 length );

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **haptic**       | the haptic device to play the rumble effect on      |
| **strength**     | strength of the rumble to play as a 0-1 float value |
| **length**       | length of the rumble to play in milliseconds        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticRumbleInit](SDL_HapticRumbleInit.md)
* [SDL_HapticRumbleStop](SDL_HapticRumbleStop.md)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported.md)

----
[CategoryAPI](CategoryAPI.md)
