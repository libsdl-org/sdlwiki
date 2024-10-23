###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_StopHapticEffect

Stop the haptic effect on its associated haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_StopHapticEffect(SDL_Haptic *haptic, int effect);
```

## Function Parameters

|                            |            |                                                            |
| -------------------------- | ---------- | ---------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to stop the effect on. |
| int                        | **effect** | the ID of the haptic effect to stop.                       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_RunHapticEffect](SDL_RunHapticEffect)
- [SDL_StopHapticEffects](SDL_StopHapticEffects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

