###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderClipEnabled

Get whether clipping is enabled on the given renderer.

## Syntax

```c
SDL_bool SDL_RenderClipEnabled(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if clipping is enabled or
[SDL_FALSE](SDL_FALSE) if not; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderClipRect](SDL_GetRenderClipRect)
* [SDL_SetRenderClipRect](SDL_SetRenderClipRect)

----
[CategoryAPI](CategoryAPI)

