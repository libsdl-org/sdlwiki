# SDL_RunHapticEffect

Run the haptic effect on its associated haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_RunHapticEffect(SDL_Haptic *haptic, SDL_HapticEffectID effect, Uint32 iterations);
```

## Function Parameters

|                                          |                |                                                                                                                 |
| ---------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) *               | **haptic**     | the [SDL_Haptic](SDL_Haptic) device to run the effect on.                                                       |
| [SDL_HapticEffectID](SDL_HapticEffectID) | **effect**     | the ID of the haptic effect to run.                                                                             |
| [Uint32](Uint32)                         | **iterations** | the number of iterations to run the effect; use [`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY) to repeat forever. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

To repeat the effect over and over indefinitely, set `iterations` to
[`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY). (Repeats the envelope -
attack and fade.) To make one instance of the effect last indefinitely (so
the effect does not fade), set the effect's `length` in its structure/union
to [`SDL_HAPTIC_INFINITY`](SDL_HAPTIC_INFINITY) instead.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetHapticEffectStatus](SDL_GetHapticEffectStatus)
- [SDL_StopHapticEffect](SDL_StopHapticEffect)
- [SDL_StopHapticEffects](SDL_StopHapticEffects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

