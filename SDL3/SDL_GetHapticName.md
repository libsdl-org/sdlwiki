###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHapticName

Get the implementation dependent name of a haptic device.

## Syntax

```c
const char* SDL_GetHapticName(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                                                                   |
| -------------- | --------------------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the name of the selected haptic device. If no name can be found,
this function returns NULL; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetHapticInstanceName](SDL_GetHapticInstanceName)
* [SDL_OpenHaptic](SDL_OpenHaptic)

----
[CategoryAPI](CategoryAPI)

