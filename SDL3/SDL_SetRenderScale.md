###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderScale

Set the drawing scale for rendering on the current target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_SetRenderScale(SDL_Renderer *renderer, float scaleX, float scaleY);

```

## Function Parameters

|                  |                               |
| ---------------- | ----------------------------- |
| **renderer**     | the rendering context         |
| **scaleX**       | the horizontal scaling factor |
| **scaleY**       | the vertical scaling factor   |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The drawing coordinates are scaled by the x/y scaling factors before they
are used by the renderer. This allows resolution independent drawing with a
single coordinate system.

If this results in scaling or subpixel drawing by the rendering backend, it
will be handled using the appropriate quality hints. For best results use
integer scaling factors.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetRenderScale](SDL_GetRenderScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

