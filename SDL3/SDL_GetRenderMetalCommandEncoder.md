###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderMetalCommandEncoder

Get the Metal command encoder for the current frame 

## Syntax

```c
void* SDL_GetRenderMetalCommandEncoder(SDL_Renderer *renderer);

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
render targets, just the window's backbacker. Check your return values!

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderMetalLayer](SDL_GetRenderMetalLayer)

----
[CategoryAPI](CategoryAPI)

