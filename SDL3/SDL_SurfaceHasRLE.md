# SDL_SurfaceHasRLE

Returns whether the surface is RLE enabled.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SurfaceHasRLE(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                    |
| ---------------------------- | ----------- | -------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query. |

## Return Value

(bool) Returns true if the surface is RLE enabled, false otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return false.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetSurfaceRLE](SDL_SetSurfaceRLE)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

