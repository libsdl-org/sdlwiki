###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetMetalCommandEncoder

Get the Metal command encoder for the current frame

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void* SDL_RenderGetMetalCommandEncoder(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | The renderer to query |

## Return Value

Returns an `id<MTLRenderCommandEncoder>` on success, or NULL if the
renderer isn't a Metal renderer or there was an error.

## Remarks

This function returns `void *`, so SDL doesn't have to include Metal's
headers, but it can be safely cast to an `id<MTLRenderCommandEncoder>`.

Note that as of SDL 2.0.18, this will return NULL if Metal refuses to give
SDL a drawable to render to, which might happen if the window is
hidden/minimized/offscreen. This doesn't apply to command encoders for
render targets, just the window's backbuffer. Check your return values!

## Version

This function is available since SDL 2.0.8.

## See Also

* [SDL_RenderGetMetalLayer](SDL_RenderGetMetalLayer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

