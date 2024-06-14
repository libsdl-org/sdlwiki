###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HapticEffectSupported

Check to see if an effect is supported by a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_bool SDL_HapticEffectSupported(SDL_Haptic *haptic, const SDL_HapticEffect *effect);
```

## Function Parameters

|                                              |            |                                               |
| -------------------------------------------- | ---------- | --------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) *                   | **haptic** | the [SDL_Haptic](SDL_Haptic) device to query. |
| const [SDL_HapticEffect](SDL_HapticEffect) * | **effect** | the desired effect to query.                  |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the effect is
supported or [SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateHapticEffect](SDL_CreateHapticEffect)
- [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

