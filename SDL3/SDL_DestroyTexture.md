# SDL_DestroyTexture

Destroy the specified texture.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_DestroyTexture(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                         |
| ---------------------------- | ----------- | ----------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to destroy. |

## Remarks

Passing NULL or an otherwise invalid texture will set the SDL error message
to "Invalid texture".

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTexture](SDL_CreateTexture)
- [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

