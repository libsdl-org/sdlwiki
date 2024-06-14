###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseHaptic

Close a haptic device previously opened with [SDL_OpenHaptic](SDL_OpenHaptic)().

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
void SDL_CloseHaptic(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                               |
| -------------------------- | ---------- | --------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to close. |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenHaptic](SDL_OpenHaptic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

