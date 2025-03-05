# SDL_GetSurfaceBlendMode

Get the blend mode used for blit operations.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_GetSurfaceBlendMode(SDL_Surface *surface, SDL_BlendMode *blendMode);
```

## Function Parameters

|                                  |               |                                                                      |
| -------------------------------- | ------------- | -------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) *     | **surface**   | the [SDL_Surface](SDL_Surface) structure to query.                   |
| [SDL_BlendMode](SDL_BlendMode) * | **blendMode** | a pointer filled in with the current [SDL_BlendMode](SDL_BlendMode). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetSurfaceBlendMode](SDL_SetSurfaceBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

