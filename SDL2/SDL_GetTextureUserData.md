# SDL_GetTextureUserData

Get the user-specified pointer associated with a texture

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
void * SDL_GetTextureUserData(SDL_Texture * texture);
```

## Function Parameters

|                              |             |                       |
| ---------------------------- | ----------- | --------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query. |

## Return Value

(void *) Return the pointer associated with the texture, or NULL if the
texture is not valid.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_SetTextureUserData](SDL_SetTextureUserData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

