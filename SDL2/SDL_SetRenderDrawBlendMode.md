###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetRenderDrawBlendMode

Set the blend mode used for drawing operations (Fill and Line).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_SetRenderDrawBlendMode(SDL_Renderer * renderer,
                               SDL_BlendMode blendMode);

```

## Function Parameters

|                   |                                                        |
| ----------------- | ------------------------------------------------------ |
| **renderer**      | the rendering context                                  |
| **blendMode**     | the [SDL_BlendMode](SDL_BlendMode) to use for blending |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the blend mode is not supported, the closest supported mode is chosen.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetRenderDrawBlendMode](SDL_GetRenderDrawBlendMode)
- [SDL_RenderDrawLine](SDL_RenderDrawLine)
- [SDL_RenderDrawLines](SDL_RenderDrawLines)
- [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
- [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
- [SDL_RenderDrawRect](SDL_RenderDrawRect)
- [SDL_RenderDrawRects](SDL_RenderDrawRects)
- [SDL_RenderFillRect](SDL_RenderFillRect)
- [SDL_RenderFillRects](SDL_RenderFillRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

