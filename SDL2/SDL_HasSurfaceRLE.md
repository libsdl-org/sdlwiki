###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasSurfaceRLE

Returns whether the surface is RLE enabled

## Syntax

```c
SDL_bool SDL_HasSurfaceRLE(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the surface is RLE enabled,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return
[SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 2.0.14.

## Related Functions

* [SDL_SetSurfaceRLE](SDL_SetSurfaceRLE.md)

----
[CategoryAPI](CategoryAPI.md)
