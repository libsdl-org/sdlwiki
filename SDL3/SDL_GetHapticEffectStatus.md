###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetHapticEffectStatus

Get the status of the current effect on the specified haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_GetHapticEffectStatus(SDL_Haptic *haptic, int effect);
```

## Function Parameters

|                            |            |                                                                        |
| -------------------------- | ---------- | ---------------------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to query for the effect status on. |
| int                        | **effect** | the ID of the haptic effect to query its status.                       |

## Return Value

(bool) Returns true if it is playing, false if it isn't playing or haptic
status isn't supported.

## Remarks

Device must support the [SDL_HAPTIC_STATUS](SDL_HAPTIC_STATUS) feature.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

