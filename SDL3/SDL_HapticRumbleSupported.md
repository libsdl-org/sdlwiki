# SDL_HapticRumbleSupported

Check whether rumble is supported on a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_HapticRumbleSupported(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                            |
| -------------------------- | ---------- | ------------------------------------------ |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | haptic device to check for rumble support. |

## Return Value

(bool) Returns true if the effect is supported or false if it isn't.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_InitHapticRumble](SDL_InitHapticRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

