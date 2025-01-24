# SDL_InitHapticRumble

Initialize a haptic device for simple rumble playback.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_InitHapticRumble(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                                             |
| -------------------------- | ---------- | ----------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the haptic device to initialize for simple rumble playback. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PlayHapticRumble](SDL_PlayHapticRumble)
- [SDL_StopHapticRumble](SDL_StopHapticRumble)
- [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

