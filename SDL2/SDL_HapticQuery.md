###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticQuery

Get the haptic device's supported features in bitwise manner.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
unsigned int SDL_HapticQuery(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |

## Return Value

Returns a list of supported haptic features in bitwise manner (OR'd), or 0
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_HapticEffectSupported](SDL_HapticEffectSupported)
* [SDL_HapticNumEffects](SDL_HapticNumEffects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

