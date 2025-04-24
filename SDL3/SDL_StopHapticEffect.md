# SDL_StopHapticEffect

Stop the haptic effect on its associated haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_StopHapticEffect(SDL_Haptic *haptic, SDL_HapticEffectID effect);
```

## Function Parameters

|                                          |            |                                                            |
| ---------------------------------------- | ---------- | ---------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) *               | **haptic** | the [SDL_Haptic](SDL_Haptic) device to stop the effect on. |
| [SDL_HapticEffectID](SDL_HapticEffectID) | **effect** | the ID of the haptic effect to stop.                       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RunHapticEffect](SDL_RunHapticEffect)
- [SDL_StopHapticEffects](SDL_StopHapticEffects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

