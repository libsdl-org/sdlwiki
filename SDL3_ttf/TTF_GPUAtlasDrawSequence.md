###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GPUAtlasDrawSequence

Draw sequence returned by [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData)

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef struct TTF_GPUAtlasDrawSequence
{
    SDL_GPUTexture *atlas_texture;          /**< Texture atlas that stores the glyphs */
    float *xy;                              /**< Vertex positions */
    int xy_stride;                          /**< Byte size to move from one element to the next element */
    float *uv;                              /**< Vertex normalized texture coordinates */
    int uv_stride;                          /**< Byte size to move from one element to the next element */
    int num_vertices;                       /**< Number of vertices */
    int *indices;                           /**< An array of indices into the 'vertices' arrays */
    int num_indices;                        /**< Number of indices */

    struct TTF_GPUAtlasDrawSequence *next;  /**< The next sequence (will be NULL in case of the last sequence) */
} TTF_GPUAtlasDrawSequence;
```

## Version

This struct is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLTTF](CategorySDLTTF)

