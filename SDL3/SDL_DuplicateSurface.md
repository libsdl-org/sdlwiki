# SDL_DuplicateSurface

Creates a new surface identical to the existing surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_DuplicateSurface(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                           |
| ---------------------------- | ----------- | ------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to duplicate. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a copy of the surface or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the original surface has alternate images, the new surface will have a
reference to them as well.

The returned surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)().

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

