###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetSurfaceColorMod

Set an additional color value multiplied into blit operations.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetSurfaceColorMod(SDL_Surface * surface,
                           Uint8 r, Uint8 g, Uint8 b);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to update    |
| **r**           | the red color value multiplied into blit operations   |
| **g**           | the green color value multiplied into blit operations |
| **b**           | the blue color value multiplied into blit operations  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this surface is blitted, during the blit operation each source color
channel is modulated by the appropriate color value according to the
following formula:

`srcC = srcC * (color / 255)`

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetSurfaceColorMod](SDL_GetSurfaceColorMod)
* [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod)

----
[CategoryAPI](CategoryAPI)

