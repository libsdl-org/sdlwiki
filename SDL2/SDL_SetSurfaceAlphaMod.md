###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetSurfaceAlphaMod

Set an additional alpha value used in blit operations.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetSurfaceAlphaMod(SDL_Surface * surface,
                           Uint8 alpha);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to update |
| **alpha**       | the alpha value multiplied into blit operations    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this surface is blitted, during the blit operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * (alpha / 255)`

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetSurfaceAlphaMod](SDL_GetSurfaceAlphaMod)
* [SDL_SetSurfaceColorMod](SDL_SetSurfaceColorMod)

----
[CategoryAPI](CategoryAPI)

