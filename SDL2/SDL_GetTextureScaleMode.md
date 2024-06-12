###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTextureScaleMode

Get the scale mode used for texture scale operations.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GetTextureScaleMode(SDL_Texture * texture,
                        SDL_ScaleMode *scaleMode);
```

## Function Parameters

|                                  |               |                                                  |
| -------------------------------- | ------------- | ------------------------------------------------ |
| [SDL_Texture](SDL_Texture) *     | **texture**   | the texture to query.                            |
| [SDL_ScaleMode](SDL_ScaleMode) * | **scaleMode** | a pointer filled in with the current scale mode. |

## Return Value

(int) Return 0 on success, or -1 if the texture is not valid.

## Version

This function is available since SDL 2.0.12.

## See Also

- [SDL_SetTextureScaleMode](SDL_SetTextureScaleMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

