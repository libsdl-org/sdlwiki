###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetScale

Get the drawing scale for the current target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_RenderGetScale(SDL_Renderer * renderer,
                       float *scaleX, float *scaleY);

```

## Function Parameters

|                  |                                                         |
| ---------------- | ------------------------------------------------------- |
| **renderer**     | the renderer from which drawing scale should be queried |
| **scaleX**       | a pointer filled in with the horizontal scaling factor  |
| **scaleY**       | a pointer filled in with the vertical scaling factor    |

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_RenderSetScale](SDL_RenderSetScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

