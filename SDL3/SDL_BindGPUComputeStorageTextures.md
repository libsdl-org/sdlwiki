###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUComputeStorageTextures

Binds storage textures as readonly for use on the compute pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUComputeStorageTextures(
    SDL_GPUComputePass *computePass,
    Uint32 firstSlot,
    SDL_GPUTexture **storageTextures,
    Uint32 bindingCount);
```

## Function Parameters

|                                            |                     |                                                         |
| ------------------------------------------ | ------------------- | ------------------------------------------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) * | **computePass**     | a compute pass handle.                                  |
| Uint32                                     | **firstSlot**       | the compute storage texture slot to begin binding from. |
| [SDL_GPUTexture](SDL_GPUTexture) **        | **storageTextures** | an array of storage textures.                           |
| Uint32                                     | **bindingCount**    | the number of storage textures to bind from the array.  |

## Remarks

These textures must have been created with
[SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ](SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

