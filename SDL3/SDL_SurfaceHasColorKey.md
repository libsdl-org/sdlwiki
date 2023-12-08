###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SurfaceHasColorKey

Returns whether the surface has a color key

## Syntax

```c
SDL_bool SDL_SurfaceHasColorKey(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the surface has a color key,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return
[SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetSurfaceColorKey](SDL_SetSurfaceColorKey.md)
* [SDL_GetSurfaceColorKey](SDL_GetSurfaceColorKey.md)

----
[CategoryAPI](CategoryAPI.md)
