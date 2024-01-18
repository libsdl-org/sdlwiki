###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StopHapticRumble

Stop the simple rumble on a haptic device.

## Syntax

```c
int SDL_StopHapticRumble(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **haptic**     | the haptic device to stop the rumble effect on |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_InitHapticRumble](SDL_InitHapticRumble)
* [SDL_PlayHapticRumble](SDL_PlayHapticRumble)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)

----
[CategoryAPI](CategoryAPI)

