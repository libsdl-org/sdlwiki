###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawBlendMode

Set the blend mode used for drawing operations (Fill and Line).

## Syntax

```c
int SDL_SetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode blendMode);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderDrawBlendMode](SDL_GetRenderDrawBlendMode.md)
* [SDL_RenderLine](SDL_RenderLine.md)
* [SDL_RenderLines](SDL_RenderLines.md)
* [SDL_RenderPoint](SDL_RenderPoint.md)
* [SDL_RenderPoints](SDL_RenderPoints.md)
* [SDL_RenderRect](SDL_RenderRect.md)
* [SDL_RenderRects](SDL_RenderRects.md)
* [SDL_RenderFillRect](SDL_RenderFillRect.md)
* [SDL_RenderFillRects](SDL_RenderFillRects.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
