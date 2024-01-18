###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHapticInstanceID

Get the instance ID of an opened haptic device.

## Syntax

```c
SDL_HapticID SDL_GetHapticInstanceID(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |

## Return Value

Returns the instance ID of the specified haptic device on success or 0 on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenHaptic](SDL_OpenHaptic)

----
[CategoryAPI](CategoryAPI)

