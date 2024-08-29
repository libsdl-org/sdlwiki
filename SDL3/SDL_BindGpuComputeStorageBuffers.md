###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGpuComputeStorageBuffers

Binds storage buffers as readonly for use on the compute pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGpuComputeStorageBuffers(
    SDL_GpuComputePass *computePass,
    Uint32 firstSlot,
    SDL_GpuBuffer **storageBuffers,
    Uint32 bindingCount);
```

## Function Parameters

|                                            |                    |                                                        |
| ------------------------------------------ | ------------------ | ------------------------------------------------------ |
| [SDL_GpuComputePass](SDL_GpuComputePass) * | **computePass**    | a compute pass handle.                                 |
| Uint32                                     | **firstSlot**      | the compute storage buffer slot to begin binding from. |
| [SDL_GpuBuffer](SDL_GpuBuffer) **          | **storageBuffers** | an array of storage buffer binding structs.            |
| Uint32                                     | **bindingCount**   | the number of storage buffers to bind from the array.  |

## Remarks

These buffers must have been created with
[SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ_BIT](SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ_BIT).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


