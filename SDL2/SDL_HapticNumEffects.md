###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticNumEffects

Get the number of effects a haptic device can store.

## Syntax

```c
int SDL_HapticNumEffects(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |

## Return Value

Returns the number of effects the haptic device can store or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

On some platforms this isn't fully supported, and therefore is an
approximation. Always check to see if your created effect was actually
created and do not rely solely on
[SDL_HapticNumEffects](SDL_HapticNumEffects.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticNumEffectsPlaying](SDL_HapticNumEffectsPlaying.md)
* [SDL_HapticQuery](SDL_HapticQuery.md)

----
[CategoryAPI](CategoryAPI.md)
