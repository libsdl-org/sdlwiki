###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StopHapticEffects

Stop all the currently playing effects on a haptic device.

## Syntax

```c
int SDL_StopHapticEffects(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to stop |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

