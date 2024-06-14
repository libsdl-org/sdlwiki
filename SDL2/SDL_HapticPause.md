###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticPause

Pause a haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_HapticPause(SDL_Haptic * haptic);
```

## Function Parameters

|                            |            |                                               |
| -------------------------- | ---------- | --------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to pause. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the [`SDL_HAPTIC_PAUSE`](SDL_HAPTIC_PAUSE) feature.
Call [SDL_HapticUnpause](SDL_HapticUnpause)() to resume playback.

Do not modify the effects nor add new ones while the device is paused. That
can cause all sorts of weird errors.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_HapticUnpause](SDL_HapticUnpause)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

