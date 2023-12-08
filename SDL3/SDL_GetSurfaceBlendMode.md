###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceBlendMode

Get the blend mode used for blit operations.

## Syntax

```c
int SDL_GetSurfaceBlendMode(SDL_Surface *surface,
                            SDL_BlendMode *blendMode);

```

## Function Parameters

|                   |                                                                     |
| ----------------- | ------------------------------------------------------------------- |
| **surface**       | the [SDL_Surface](SDL_Surface.md) structure to query                   |
| **blendMode**     | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode.md) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetSurfaceBlendMode](SDL_SetSurfaceBlendMode.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
