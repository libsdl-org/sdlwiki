# SDL_RemoveSurfaceAlternateImages

Remove all alternate versions of a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
void SDL_RemoveSurfaceAlternateImages(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                     |
| ---------------------------- | ----------- | --------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update. |

## Remarks

This function removes a reference from all the alternative versions,
destroying them if this is the last reference to them.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddSurfaceAlternateImage](SDL_AddSurfaceAlternateImage)
- [SDL_GetSurfaceImages](SDL_GetSurfaceImages)
- [SDL_SurfaceHasAlternateImages](SDL_SurfaceHasAlternateImages)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

