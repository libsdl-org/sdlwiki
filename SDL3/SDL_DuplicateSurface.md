###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DuplicateSurface

Creates a new surface identical to the existing surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_Surface* SDL_DuplicateSurface(SDL_Surface *surface);

```

## Function Parameters

|                 |                           |
| --------------- | ------------------------- |
| **surface**     | the surface to duplicate. |

## Return Value

Returns a copy of the surface, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The returned surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)().

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

