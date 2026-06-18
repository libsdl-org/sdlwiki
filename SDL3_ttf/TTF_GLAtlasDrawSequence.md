###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GLAtlasDrawSequence

A draw sequence in the linked list returned by [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData).

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef struct TTF_GLAtlasDrawSequence
{
    unsigned int atlas_texture;           /**< OpenGL texture name (same as GLuint), or 0 for solid fill */
    TTF_GLAtlasDrawVertex *vertices;      /**< An array of interleaved vertex data */
    int num_vertices;                     /**< Number of vertices */
    Uint16 *indices;                      /**< An array of indices into the 'vertices' array */
    int num_indices;                      /**< Number of indices */
    TTF_ImageType image_type;             /**< The image type of this draw sequence */

    struct TTF_GLAtlasDrawSequence *next; /**< The next sequence (will be NULL in case of the last sequence) */
} TTF_GLAtlasDrawSequence;
```

## Remarks

Each sequence groups primitives that share the same atlas texture and image
type, allowing them to be drawn in a single draw call.

## Version

This struct is available since SDL_ttf 3.3.0.

## See Also

- [TTF_GLAtlasDrawVertex](TTF_GLAtlasDrawVertex)
- [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLTTF](CategorySDLTTF)

