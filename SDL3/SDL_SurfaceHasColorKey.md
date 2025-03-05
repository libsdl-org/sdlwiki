# SDL_SurfaceHasColorKey

Returns whether the surface has a color key.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SurfaceHasColorKey(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                    |
| ---------------------------- | ----------- | -------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query. |

## Return Value

(bool) Returns true if the surface has a color key, false otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return false.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetSurfaceColorKey](SDL_SetSurfaceColorKey)
- [SDL_GetSurfaceColorKey](SDL_GetSurfaceColorKey)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

