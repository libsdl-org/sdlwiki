###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextureAlphaMod

Set an additional alpha value multiplied into render copy operations.

## Syntax

```c
int SDL_SetTextureAlphaMod(SDL_Texture * texture,
                           Uint8 alpha);

```

## Function Parameters

|                 |                                                        |
| --------------- | ------------------------------------------------------ |
| **texture**     | the texture to update                                  |
| **alpha**       | the source alpha value multiplied into copy operations |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

When this texture is rendered, during the copy operation the source alpha
value is modulated by this alpha value according to the following formula:

`srcA = srcA * (alpha / 255)`

Alpha modulation is not always supported by the renderer; it will return -1
if alpha modulation is not supported.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetTextureAlphaMod](SDL_GetTextureAlphaMod.md)
* [SDL_SetTextureColorMod](SDL_SetTextureColorMod.md)

----
[CategoryAPI](CategoryAPI.md)
