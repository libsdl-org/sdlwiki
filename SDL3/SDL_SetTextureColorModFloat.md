###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTextureColorModFloat

Set an additional color value multiplied into render copy operations.

## Syntax

```c
int SDL_SetTextureColorModFloat(SDL_Texture *texture, float r, float g, float b);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **texture**     | the texture to update                                 |
| **r**           | the red color value multiplied into copy operations   |
| **g**           | the green color value multiplied into copy operations |
| **b**           | the blue color value multiplied into copy operations  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When this texture is rendered, during the copy operation each source color
channel is modulated by the appropriate color value according to the
following formula:

`srcC = srcC * color`

Color modulation is not always supported by the renderer; it will return -1
if color modulation is not supported.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTextureColorModFloat](SDL_GetTextureColorModFloat)
* [SDL_SetTextureAlphaModFloat](SDL_SetTextureAlphaModFloat)
* [SDL_SetTextureColorMod](SDL_SetTextureColorMod)

----
[CategoryAPI](CategoryAPI)

