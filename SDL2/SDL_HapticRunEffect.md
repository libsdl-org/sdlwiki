###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticRunEffect

Run the haptic effect on its associated haptic device.

## Syntax

```c
int SDL_HapticRunEffect(SDL_Haptic * haptic,
                        int effect,
                        Uint32 iterations);

```

## Function Parameters

|                    |                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| **haptic**         | the [SDL_Haptic](SDL_Haptic.md) device to run the effect on                                                       |
| **effect**         | the ID of the haptic effect to run                                                                             |
| **iterations**     | the number of iterations to run the effect; use [`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY) to repeat forever |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

To repeat the effect over and over indefinitely, set `iterations` to
[`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY). (Repeats the envelope -
attack and fade.) To make one instance of the effect last indefinitely (so
the effect does not fade), set the effect's `length` in its structure/union
to [`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY) instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticDestroyEffect](SDL_HapticDestroyEffect.md)
* [SDL_HapticGetEffectStatus](SDL_HapticGetEffectStatus.md)
* [SDL_HapticStopEffect](SDL_HapticStopEffect.md)

----
[CategoryAPI](CategoryAPI.md)
