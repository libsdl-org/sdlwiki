###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GLAtlasDrawVertex

A vertex in the draw data returned by [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData).

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef struct TTF_GLAtlasDrawVertex
{
    SDL_FPoint position; /**< Vertex position */
    SDL_FPoint texcoord; /**< Texture coordinate, or normalized rectangle coordinate for solid fill */
} TTF_GLAtlasDrawVertex;
```

## Version

This struct is available since SDL_ttf 3.3.0.

## See Also

- [TTF_GLAtlasDrawSequence](TTF_GLAtlasDrawSequence)
- [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLTTF](CategorySDLTTF)

