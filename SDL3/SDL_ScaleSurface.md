# SDL_ScaleSurface

Creates a new surface identical to the existing surface, scaled to the desired size.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_ScaleSurface(SDL_Surface *surface, int width, int height, SDL_ScaleMode scaleMode);
```

## Function Parameters

|                                |               |                                                |
| ------------------------------ | ------------- | ---------------------------------------------- |
| [SDL_Surface](SDL_Surface) *   | **surface**   | the surface to duplicate and scale.            |
| int                            | **width**     | the width of the new surface.                  |
| int                            | **height**    | the height of the new surface.                 |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode** | the [SDL_ScaleMode](SDL_ScaleMode) to be used. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a copy of the surface or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

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

