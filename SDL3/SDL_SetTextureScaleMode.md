###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTextureScaleMode

Set the scale mode used for texture scale operations.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode scaleMode);
```

## Function Parameters

|                                |               |                                                                |
| ------------------------------ | ------------- | -------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) *   | **texture**   | the texture to update.                                         |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode** | the [SDL_ScaleMode](SDL_ScaleMode) to use for texture scaling. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The default texture scale mode is
[SDL_SCALEMODE_LINEAR](SDL_SCALEMODE_LINEAR).

If the scale mode is not supported, the closest supported mode is chosen.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetTextureScaleMode](SDL_GetTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

