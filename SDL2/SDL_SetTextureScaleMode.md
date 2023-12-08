###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextureScaleMode

Set the scale mode used for texture scale operations.

## Syntax

```c
int SDL_SetTextureScaleMode(SDL_Texture * texture,
                            SDL_ScaleMode scaleMode);

```

## Function Parameters

|                   |                                                                |
| ----------------- | -------------------------------------------------------------- |
| **texture**       | The texture to update.                                         |
| **scaleMode**     | the [SDL_ScaleMode](SDL_ScaleMode.md) to use for texture scaling. |

## Return Value

Returns 0 on success, or -1 if the texture is not valid.

## Remarks

If the scale mode is not supported, the closest supported mode is chosen.

## Version

This function is available since SDL 2.0.12.

## Related Functions

* [SDL_GetTextureScaleMode](SDL_GetTextureScaleMode.md)

----
[CategoryAPI](CategoryAPI.md)
