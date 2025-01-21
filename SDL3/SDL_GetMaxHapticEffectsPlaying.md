###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetMaxHapticEffectsPlaying

Get the number of effects a haptic device can play at the same time.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
int SDL_GetMaxHapticEffectsPlaying(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                                                       |
| -------------------------- | ---------- | --------------------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to query maximum playing effects. |

## Return Value

(int) Returns the number of effects the haptic device can play at the same
time or -1 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This is not supported on all platforms, but will always return a value.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetMaxHapticEffects](SDL_GetMaxHapticEffects)
- [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

