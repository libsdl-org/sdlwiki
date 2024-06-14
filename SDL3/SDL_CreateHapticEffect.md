###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateHapticEffect

Create a new haptic effect on a specified device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
int SDL_CreateHapticEffect(SDL_Haptic *haptic, const SDL_HapticEffect *effect);
```

## Function Parameters

|                                              |            |                                                                                                      |
| -------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) *                   | **haptic** | an [SDL_Haptic](SDL_Haptic) device to create the effect on.                                          |
| const [SDL_HapticEffect](SDL_HapticEffect) * | **effect** | an [SDL_HapticEffect](SDL_HapticEffect) structure containing the properties of the effect to create. |

## Return Value

(int) Returns the ID of the effect on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DestroyHapticEffect](SDL_DestroyHapticEffect)
- [SDL_RunHapticEffect](SDL_RunHapticEffect)
- [SDL_UpdateHapticEffect](SDL_UpdateHapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

