###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextureScaleMode

Set the scale mode used for texture scale operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_SetTextureScaleMode(SDL_Texture * texture,
                            SDL_ScaleMode scaleMode);

```

## Function Parameters

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **texture**       | The texture to update.                                         |
| **scaleMode**     | the [SDL_ScaleMode](SDL_ScaleMode) to use for texture scaling. |

## Return Value

Returns 0 on success, or -1 if the texture is not valid.

## Remarks

If the scale mode is not supported, the closest supported mode is chosen.

## Version

This function is available since SDL 2.0.12.

## See Also

- [SDL_GetTextureScaleMode](SDL_GetTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

