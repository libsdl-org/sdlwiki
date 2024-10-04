###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUStorageTextureReadWriteBinding

A structure specifying parameters related to binding textures in a compute pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUStorageTextureReadWriteBinding
{
    SDL_GPUTexture *texture;  /**< The texture to bind. Must have been created with SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE or SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE. */
    Uint32 mip_level;         /**< The mip level index to bind. */
    Uint32 layer;             /**< The layer index to bind. */
    bool cycle;               /**< true cycles the texture if it is already bound. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUStorageTextureReadWriteBinding;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_BeginGPUComputePass](SDL_BeginGPUComputePass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

