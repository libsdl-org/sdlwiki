###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfaceAlphaMod

Set an additional alpha value used in blit operations.

## Syntax

```c
int SDL_SetSurfaceAlphaMod(SDL_Surface *surface,
                           Uint8 alpha);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to update |
| **alpha**       | the alpha value multiplied into blit operations    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

When this surface is blitted, during the blit operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * (alpha / 255)`

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetSurfaceAlphaMod](SDL_GetSurfaceAlphaMod.md)
* [SDL_SetSurfaceColorMod](SDL_SetSurfaceColorMod.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
