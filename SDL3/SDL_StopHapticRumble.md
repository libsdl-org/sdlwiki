# SDL_StopHapticRumble

Stop the simple rumble on a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_StopHapticRumble(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                                 |
| -------------------------- | ---------- | ----------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the haptic device to stop the rumble effect on. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PlayHapticRumble](SDL_PlayHapticRumble)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

