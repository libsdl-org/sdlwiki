###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderMetalCommandEncoder

Get the Metal command encoder for the current frame.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void* SDL_GetRenderMetalCommandEncoder(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                       |
| ------------------------------ | ------------ | --------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | The renderer to query |

## Return Value

(void *) Returns an `id<MTLRenderCommandEncoder>` on success, or NULL if
the renderer isn't a Metal renderer or there was an error.

## Remarks

This function returns `void *`, so SDL doesn't have to include Metal's
headers, but it can be safely cast to an `id<MTLRenderCommandEncoder>`.

This will return NULL if Metal refuses to give SDL a drawable to render to,
which might happen if the window is hidden/minimized/offscreen. This
doesn't apply to command encoders for render targets, just the window's
backbuffer. Check your return values!

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderMetalLayer](SDL_GetRenderMetalLayer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

