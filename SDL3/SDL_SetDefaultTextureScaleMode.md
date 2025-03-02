# SDL_SetDefaultTextureScaleMode

Set default scale mode for new textures for given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetDefaultTextureScaleMode(SDL_Renderer *renderer, SDL_ScaleMode scale_mode);
```

## Function Parameters

|                                |                |                                               |
| ------------------------------ | -------------- | --------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer**   | the renderer to update.                       |
| [SDL_ScaleMode](SDL_ScaleMode) | **scale_mode** | the scale mode to change to for new textures. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When a renderer is created, scale_mode defaults to
[SDL_SCALEMODE_LINEAR](SDL_SCALEMODE_LINEAR).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_GetDefaultTextureScaleMode](SDL_GetDefaultTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

