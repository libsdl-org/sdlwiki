###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceColorMod

Get the additional color value multiplied into blit operations.

## Syntax

```c
int SDL_GetSurfaceColorMod(SDL_Surface *surface,
                           Uint8 *r, Uint8 *g,
                           Uint8 *b);

```

## Function Parameters

|                 |                                                        |
| --------------- | ------------------------------------------------------ |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to query      |
| **r**           | a pointer filled in with the current red color value   |
| **g**           | a pointer filled in with the current green color value |
| **b**           | a pointer filled in with the current blue color value  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetSurfaceAlphaMod](SDL_GetSurfaceAlphaMod.md)
* [SDL_SetSurfaceColorMod](SDL_SetSurfaceColorMod.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
