# SDL_GetRenderTarget

Get the current render target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Return Value

([SDL_Texture](SDL_Texture) *) Returns the current render target or NULL
for the default render target.

## Remarks

The default render target is the window for which the renderer was created,
and is reported as NULL here.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetRenderTarget](SDL_SetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

