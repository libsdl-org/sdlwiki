# SDL_PauseHaptic

Pause a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_PauseHaptic(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                               |
| -------------------------- | ---------- | --------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to pause. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the [`SDL_HAPTIC_PAUSE`](SDL_HAPTIC_PAUSE) feature.
Call [SDL_ResumeHaptic](SDL_ResumeHaptic)() to resume playback.

Do not modify the effects nor add new ones while the device is paused. That
can cause all sorts of weird errors.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ResumeHaptic](SDL_ResumeHaptic)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

