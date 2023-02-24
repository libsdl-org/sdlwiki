###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasColorKey

Returns whether the surface has a color key 

## Syntax

```c
SDL_bool SDL_HasColorKey(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to query |

## Return Value

Return [SDL_TRUE](SDL_TRUE) if the surface has a color key,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

It is safe to pass a NULL `surface` here; it will return
[SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 2.0.9.

## Related Functions

* [SDL_SetColorKey](SDL_SetColorKey)
* [SDL_GetColorKey](SDL_GetColorKey)

----
[CategoryAPI](CategoryAPI)

