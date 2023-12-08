###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderIsClipEnabled

Get whether clipping is enabled on the given renderer.

## Syntax

```c
SDL_bool SDL_RenderIsClipEnabled(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                                                      |
| ---------------- | ---------------------------------------------------- |
| **renderer**     | the renderer from which clip state should be queried |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if clipping is enabled or
[SDL_FALSE](SDL_FALSE.md) if not; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Version

This function is available since SDL 2.0.4.

## Related Functions

* [SDL_RenderGetClipRect](SDL_RenderGetClipRect.md)
* [SDL_RenderSetClipRect](SDL_RenderSetClipRect.md)

----
[CategoryAPI](CategoryAPI.md)
