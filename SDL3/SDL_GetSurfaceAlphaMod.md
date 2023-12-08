###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceAlphaMod

Get the additional alpha value used in blit operations.

## Syntax

```c
int SDL_GetSurfaceAlphaMod(SDL_Surface *surface,
                           Uint8 *alpha);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to query |
| **alpha**       | a pointer filled in with the current alpha value  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetSurfaceColorMod](SDL_GetSurfaceColorMod.md)
* [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
