###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticNewEffect

Create a new haptic effect on a specified device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_HapticNewEffect(SDL_Haptic * haptic,
                        SDL_HapticEffect * effect);

```

## Function Parameters

|                |                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------- |
| **haptic**     | an [SDL_Haptic](SDL_Haptic) device to create the effect on                                          |
| **effect**     | an [SDL_HapticEffect](SDL_HapticEffect) structure containing the properties of the effect to create |

## Return Value

Returns the ID of the effect on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticDestroyEffect](SDL_HapticDestroyEffect)
* [SDL_HapticRunEffect](SDL_HapticRunEffect)
* [SDL_HapticUpdateEffect](SDL_HapticUpdateEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


