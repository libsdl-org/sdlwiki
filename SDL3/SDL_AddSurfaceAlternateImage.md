# SDL_AddSurfaceAlternateImage

Add an alternate version of a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_AddSurfaceAlternateImage(SDL_Surface *surface, SDL_Surface *image);
```

## Function Parameters

|                              |             |                                                                                      |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update.                                  |
| [SDL_Surface](SDL_Surface) * | **image**   | a pointer to an alternate [SDL_Surface](SDL_Surface) to associate with this surface. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function adds an alternate version of this surface, usually used for
content with high DPI representations like cursors or icons. The size,
format, and content do not need to match the original surface, and these
alternate versions will not be updated when the original surface changes.

This function adds a reference to the alternate version, so you should call
[SDL_DestroySurface](SDL_DestroySurface)() on the image after this call.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RemoveSurfaceAlternateImages](SDL_RemoveSurfaceAlternateImages)
- [SDL_GetSurfaceImages](SDL_GetSurfaceImages)
- [SDL_SurfaceHasAlternateImages](SDL_SurfaceHasAlternateImages)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

