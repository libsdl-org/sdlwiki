###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticQuery

Get the haptic device's supported features in bitwise manner.

## Syntax

```c
unsigned int SDL_HapticQuery(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |

## Return Value

Returns a list of supported haptic features in bitwise manner (OR'd), or 0
on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_Haptic *haptic;
if (SDL_HapticQuery(haptic) & SDL_HAPTIC_CONSTANT) {
    SDL_Log("We have constant haptic effect!");
}
```

## Related Functions

* [SDL_HapticEffectSupported](SDL_HapticEffectSupported.md)
* [SDL_HapticNumEffects](SDL_HapticNumEffects.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
