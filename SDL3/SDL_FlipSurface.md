# SDL_FlipSurface

Flip a surface vertically or horizontally.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_FlipSurface(SDL_Surface *surface, SDL_FlipMode flip);
```

## Function Parameters

|                              |             |                        |
| ---------------------------- | ----------- | ---------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to flip.   |
| [SDL_FlipMode](SDL_FlipMode) | **flip**    | the direction to flip. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

