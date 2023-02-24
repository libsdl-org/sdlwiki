###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfaceBlendMode

Set the blend mode used for blit operations.

## Syntax

```c
int SDL_SetSurfaceBlendMode(SDL_Surface *surface,
                            SDL_BlendMode blendMode);

```

## Function Parameters

|                   |                                                             |
| ----------------- | ----------------------------------------------------------- |
| **surface**       | the [SDL_Surface](SDL_Surface) structure to update          |
| **blendMode**     | the [SDL_BlendMode](SDL_BlendMode) to use for blit blending |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

To copy a surface to another surface (or texture) without blending with the
existing data, the blendmode of the SOURCE surface should be set to
[`SDL_BLENDMODE_NONE`](SDL_BLENDMODE_NONE).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetSurfaceBlendMode](SDL_GetSurfaceBlendMode)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


