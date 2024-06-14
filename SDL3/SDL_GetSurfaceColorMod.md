###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceColorMod

Get the additional color value multiplied into blit operations.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
int SDL_GetSurfaceColorMod(SDL_Surface *surface, Uint8 *r, Uint8 *g, Uint8 *b);
```

## Function Parameters

|                              |             |                                                         |
| ---------------------------- | ----------- | ------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query.      |
| Uint8 *                      | **r**       | a pointer filled in with the current red color value.   |
| Uint8 *                      | **g**       | a pointer filled in with the current green color value. |
| Uint8 *                      | **b**       | a pointer filled in with the current blue color value.  |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetSurfaceAlphaMod](SDL_GetSurfaceAlphaMod)
- [SDL_SetSurfaceColorMod](SDL_SetSurfaceColorMod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

