# SDL_GetDefaultTextureScaleMode

Get default texture scale mode of the given renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetDefaultTextureScaleMode(SDL_Renderer *renderer, SDL_ScaleMode *scale_mode);
```

## Function Parameters

|                                  |                |                                                                                                                                                                               |
| -------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer**   | the renderer to get data from.                                                                                                                                                |
| [SDL_ScaleMode](SDL_ScaleMode) * | **scale_mode** | a [SDL_ScaleMode](SDL_ScaleMode) filled with current default scale mode. See [SDL_SetDefaultTextureScaleMode](SDL_SetDefaultTextureScaleMode)() for the meaning of the value. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_SetDefaultTextureScaleMode](SDL_SetDefaultTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

