###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticEffectSupported

Check to see if an effect is supported by a haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_HapticEffectSupported(SDL_Haptic * haptic,
                              SDL_HapticEffect *
                              effect);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |
| **effect**     | the desired effect to query                  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if effect is supported, [SDL_FALSE](SDL_FALSE)
if it isn't, or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticNewEffect](SDL_HapticNewEffect)
* [SDL_HapticQuery](SDL_HapticQuery)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


