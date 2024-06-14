###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StopHapticRumble

Stop the simple rumble on a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
int SDL_StopHapticRumble(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                                 |
| -------------------------- | ---------- | ----------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the haptic device to stop the rumble effect on. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PlayHapticRumble](SDL_PlayHapticRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

