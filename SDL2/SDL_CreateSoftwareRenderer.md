###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateSoftwareRenderer

Create a 2D software rendering context for a surface.

## Syntax

```c
SDL_Renderer * SDL_CreateSoftwareRenderer(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure representing the surface where rendering is done |

## Return Value

Returns a valid rendering context or NULL if there was an error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Two other API which can be used to create [SDL_Renderer](SDL_Renderer.md):
[SDL_CreateRenderer](SDL_CreateRenderer.md)() and
[SDL_CreateWindowAndRenderer](SDL_CreateWindowAndRenderer.md)(). These can
_also_ create a software renderer, but they are intended to be used with an
[SDL_Window](SDL_Window.md) as the final destination and not an
[SDL_Surface](SDL_Surface.md).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_CreateWindowRenderer](SDL_CreateWindowRenderer.md)
* [SDL_DestroyRenderer](SDL_DestroyRenderer.md)

----
[CategoryAPI](CategoryAPI.md)
