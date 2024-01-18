###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_InitHapticRumble

Initialize a haptic device for simple rumble playback.

## Syntax

```c
int SDL_InitHapticRumble(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                                            |
| -------------- | ---------------------------------------------------------- |
| **haptic**     | the haptic device to initialize for simple rumble playback |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenHaptic](SDL_OpenHaptic)
* [SDL_PlayHapticRumble](SDL_PlayHapticRumble)
* [SDL_StopHapticRumble](SDL_StopHapticRumble)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)

----
[CategoryAPI](CategoryAPI)

