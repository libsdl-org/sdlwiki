###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetMetalLayer

Get the CAMetalLayer associated with the given Metal renderer.

## Syntax

```c
void* SDL_RenderGetMetalLayer(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | The renderer to query |

## Return Value

Returns a `CAMetalLayer *` on success, or NULL if the renderer isn't a
Metal renderer

## Remarks

This function returns `void *`, so SDL doesn't have to include Metal's
headers, but it can be safely cast to a `CAMetalLayer *`.

## Version

This function is available since SDL 2.0.8.

## Related Functions

* [SDL_RenderGetMetalCommandEncoder](SDL_RenderGetMetalCommandEncoder)

----
[CategoryAPI](CategoryAPI)

