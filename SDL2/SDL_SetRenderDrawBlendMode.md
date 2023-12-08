###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetRenderDrawBlendMode

Set the blend mode used for drawing operations (Fill and Line).

## Syntax

```c
int SDL_SetRenderDrawBlendMode(SDL_Renderer * renderer,
                               SDL_BlendMode blendMode);

```

## Function Parameters

|                   |                                                        |
| ----------------- | ------------------------------------------------------ |
| **renderer**      | the rendering context                                  |
| **blendMode**     | the [SDL_BlendMode](SDL_BlendMode.md) to use for blending |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If the blend mode is not supported, the closest supported mode is chosen.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRenderDrawBlendMode](SDL_GetRenderDrawBlendMode.md)
* [SDL_RenderDrawLine](SDL_RenderDrawLine.md)
* [SDL_RenderDrawLines](SDL_RenderDrawLines.md)
* [SDL_RenderDrawPoint](SDL_RenderDrawPoint.md)
* [SDL_RenderDrawPoints](SDL_RenderDrawPoints.md)
* [SDL_RenderDrawRect](SDL_RenderDrawRect.md)
* [SDL_RenderDrawRects](SDL_RenderDrawRects.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)

----
[CategoryAPI](CategoryAPI.md)
