# SDL_GetSurfaceImages

Get an array including all versions of a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface ** SDL_GetSurfaceImages(SDL_Surface *surface, int *count);
```

## Function Parameters

|                              |             |                                                                                |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query.                             |
| int *                        | **count**   | a pointer filled in with the number of surface pointers returned, may be NULL. |

## Return Value

([SDL_Surface](SDL_Surface) **) Returns a NULL terminated array of
[SDL_Surface](SDL_Surface) pointers or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

This returns all versions of a surface, with the surface being queried as
the first element in the returned array.

Freeing the array of surfaces does not affect the surfaces in the array.
They are still referenced by the surface being queried and will be cleaned
up normally.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddSurfaceAlternateImage](SDL_AddSurfaceAlternateImage)
- [SDL_RemoveSurfaceAlternateImages](SDL_RemoveSurfaceAlternateImages)
- [SDL_SurfaceHasAlternateImages](SDL_SurfaceHasAlternateImages)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

