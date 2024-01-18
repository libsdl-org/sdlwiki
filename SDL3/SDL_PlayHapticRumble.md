###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PlayHapticRumble

Run a simple rumble effect on a haptic device.

## Syntax

```c
int SDL_PlayHapticRumble(SDL_Haptic *haptic, float strength, Uint32 length);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **haptic**       | the haptic device to play the rumble effect on      |
| **strength**     | strength of the rumble to play as a 0-1 float value |
| **length**       | length of the rumble to play in milliseconds        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_InitHapticRumble](SDL_InitHapticRumble)
* [SDL_StopHapticRumble](SDL_StopHapticRumble)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)

----
[CategoryAPI](CategoryAPI)

