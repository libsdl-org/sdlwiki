###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

## Syntax

```c
int SDL_GetTextureScaleMode(SDL_Texture * texture,
                            SDL_ScaleMode *scaleMode);

```

## Function Parameters

|                   |                                                  |
| ----------------- | ------------------------------------------------ |
| **texture**       | the texture to query.                            |
| **scaleMode**     | a pointer filled in with the current scale mode. |

## Return Value

Return 0 on success, or -1 if the texture is not valid.

## Version

This function is available since SDL 2.0.12.

## Related Functions

* [SDL_SetTextureScaleMode](SDL_SetTextureScaleMode.md)

----
[CategoryAPI](CategoryAPI.md)
