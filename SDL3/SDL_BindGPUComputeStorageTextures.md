# SDL_BindGPUComputeStorageTextures

Binds storage textures as readonly for use on the compute pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUComputeStorageTextures(
    SDL_GPUComputePass *compute_pass,
    Uint32 first_slot,
    SDL_GPUTexture *const *storage_textures,
    Uint32 num_bindings);
```

## Function Parameters

|                                            |                      |                                                         |
| ------------------------------------------ | -------------------- | ------------------------------------------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) * | **compute_pass**     | a compute pass handle.                                  |
| [Uint32](Uint32)                           | **first_slot**       | the compute storage texture slot to begin binding from. |
| [SDL_GPUTexture](SDL_GPUTexture) *const *  | **storage_textures** | an array of storage textures.                           |
| [Uint32](Uint32)                           | **num_bindings**     | the number of storage textures to bind from the array.  |

## Remarks

These textures must have been created with
[SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ](SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ).

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

