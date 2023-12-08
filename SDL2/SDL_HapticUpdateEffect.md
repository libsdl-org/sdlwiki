###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticUpdateEffect

Update the properties of an effect.

## Syntax

```c
int SDL_HapticUpdateEffect(SDL_Haptic * haptic,
                           int effect,
                           SDL_HapticEffect * data);

```

## Function Parameters

|                |                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device that has the effect                                       |
| **effect**     | the identifier of the effect to update                                                        |
| **data**       | an [SDL_HapticEffect](SDL_HapticEffect.md) structure containing the new effect properties to use |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Can be used dynamically, although behavior when dynamically changing
direction may be strange. Specifically the effect may re-upload itself and
start playing from the start. You also cannot change the type either when
running [SDL_HapticUpdateEffect](SDL_HapticUpdateEffect.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticDestroyEffect](SDL_HapticDestroyEffect.md)
* [SDL_HapticNewEffect](SDL_HapticNewEffect.md)
* [SDL_HapticRunEffect](SDL_HapticRunEffect.md)

----
[CategoryAPI](CategoryAPI.md)
