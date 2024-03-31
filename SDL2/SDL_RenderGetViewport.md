###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetViewport

Get the drawing area for the current target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_RenderGetViewport(SDL_Renderer * renderer,
                           SDL_Rect * rect);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                     |
| **rect**         | an [SDL_Rect](SDL_Rect) structure filled in with the current drawing area |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderSetViewport](SDL_RenderSetViewport)

----
[CategoryAPI](CategoryAPI)

