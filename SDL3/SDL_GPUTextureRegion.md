###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUTextureRegion

A structure specifying a region of a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUTextureRegion
{
    SDL_GPUTexture *texture;  /**< The texture used in the copy operation. */
    Uint32 mip_level;         /**< The mip level index to transfer. */
    Uint32 layer;             /**< The layer index to transfer. */
    Uint32 x;                 /**< The left offset of the region. */
    Uint32 y;                 /**< The top offset of the region. */
    Uint32 z;                 /**< The front offset of the region. */
    Uint32 w;                 /**< The width of the region. */
    Uint32 h;                 /**< The height of the region. */
    Uint32 d;                 /**< The depth of the region. */
} SDL_GPUTextureRegion;
```

## Remarks

Used when transferring data to or from a texture.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

