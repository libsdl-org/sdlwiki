###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUBlitRegion

A structure specifying a region of a texture used in the blit operation.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUBlitRegion
{
    SDL_GPUTexture *texture;  /**< The texture. */
    Uint32 mip_level;             /**< The mip level index of the region. */
    Uint32 layer_or_depth_plane;  /**< The layer index or depth plane of the region. This value is treated as a layer index on 2D array and cube textures, and as a depth plane on 3D textures. */
    Uint32 x;                     /**< The left offset of the region. */
    Uint32 y;                     /**< The top offset of the region.  */
    Uint32 w;                     /**< The width of the region. */
    Uint32 h;                     /**< The height of the region. */
} SDL_GPUBlitRegion;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_BlitGPUTexture](SDL_BlitGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

