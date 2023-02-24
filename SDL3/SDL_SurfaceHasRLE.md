###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SurfaceHasRLE

Returns whether the surface is RLE enabled 

## Syntax

```c
SDL_bool SDL_SurfaceHasRLE(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the surface is RLE enabled,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return
[SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetSurfaceRLE](SDL_SetSurfaceRLE)

----
[CategoryAPI](CategoryAPI)

