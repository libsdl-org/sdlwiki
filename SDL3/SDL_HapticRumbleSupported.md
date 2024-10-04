###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

This function is available since SDL 3.0.0.

## See Also

- [SDL_InitHapticRumble](SDL_InitHapticRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

