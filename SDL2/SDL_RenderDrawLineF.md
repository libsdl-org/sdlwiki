###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawLineF

Draw a line on the current rendering target at subpixel precision.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_RenderDrawLineF(SDL_Renderer * renderer,
                        float x1, float y1, float x2, float y2);

```

## Function Parameters

|                  |                                        |
| ---------------- | -------------------------------------- |
| **renderer**     | The renderer which should draw a line. |
| **x1**           | The x coordinate of the start point.   |
| **y1**           | The y coordinate of the start point.   |
| **x2**           | The x coordinate of the end point.     |
| **y2**           | The y coordinate of the end point.     |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

