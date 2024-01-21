###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateHapticEffect

Update the properties of an effect.

## Syntax

```c
int SDL_UpdateHapticEffect(SDL_Haptic *haptic, int effect, const SDL_HapticEffect *data);

```

## Function Parameters

|                |                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device that has the effect                                       |
| **effect**     | the identifier of the effect to update                                                        |
| **data**       | an [SDL_HapticEffect](SDL_HapticEffect) structure containing the new effect properties to use |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Can be used dynamically, although behavior when dynamically changing
direction may be strange. Specifically the effect may re-upload itself and
start playing from the start. You also cannot change the type either when
running [SDL_UpdateHapticEffect](SDL_UpdateHapticEffect)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DestroyHapticEffect](SDL_DestroyHapticEffect)
* [SDL_CreateHapticEffect](SDL_CreateHapticEffect)
* [SDL_RunHapticEffect](SDL_RunHapticEffect)

----
[CategoryAPI](CategoryAPI)

