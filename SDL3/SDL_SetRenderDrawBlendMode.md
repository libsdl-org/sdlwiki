# SDL_SetRenderDrawBlendMode

Set the blend mode used for drawing operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode blendMode);
```

## Function Parameters

|                                |               |                                                         |
| ------------------------------ | ------------- | ------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer**  | the rendering context.                                  |
| [SDL_BlendMode](SDL_BlendMode) | **blendMode** | the [SDL_BlendMode](SDL_BlendMode) to use for blending. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This blend mode is used for any drawing that doesn't involve textures.

If the blend mode is not supported, the closest supported mode is chosen.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderDrawBlendMode](SDL_GetRenderDrawBlendMode)
- [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

