###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ResumeHaptic

Resume a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_bool SDL_ResumeHaptic(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                                 |
| -------------------------- | ---------- | ----------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to unpause. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Call to unpause after [SDL_PauseHaptic](SDL_PauseHaptic)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PauseHaptic](SDL_PauseHaptic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

