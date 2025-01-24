# SDL_SurfaceHasAlternateImages

Return whether a surface has alternate versions available.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SurfaceHasAlternateImages(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                    |
| ---------------------------- | ----------- | -------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query. |

## Return Value

(bool) Returns true if alternate versions are available or false otherwise.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddSurfaceAlternateImage](SDL_AddSurfaceAlternateImage)
- [SDL_RemoveSurfaceAlternateImages](SDL_RemoveSurfaceAlternateImages)
- [SDL_GetSurfaceImages](SDL_GetSurfaceImages)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

