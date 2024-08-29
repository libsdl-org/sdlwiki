###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGpuComputeStorageTextures

Binds storage textures as readonly for use on the compute pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGpuComputeStorageTextures(
    SDL_GpuComputePass *computePass,
    Uint32 firstSlot,
    SDL_GpuTexture **storageTextures,
    Uint32 bindingCount);
```

## Function Parameters

|                                            |                     |                                                         |
| ------------------------------------------ | ------------------- | ------------------------------------------------------- |
| [SDL_GpuComputePass](SDL_GpuComputePass) * | **computePass**     | a compute pass handle.                                  |
| Uint32                                     | **firstSlot**       | the compute storage texture slot to begin binding from. |
| [SDL_GpuTexture](SDL_GpuTexture) **        | **storageTextures** | an array of storage textures.                           |
| Uint32                                     | **bindingCount**    | the number of storage textures to bind from the array.  |

## Remarks

These textures must have been created with
[SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ_BIT](SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ_BIT).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

