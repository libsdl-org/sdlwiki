###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUVertexStorageBuffers

Binds storage buffers for use on the vertex shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUVertexStorageBuffers(
    SDL_GPURenderPass *renderPass,
    Uint32 firstSlot,
    SDL_GPUBuffer *const *storageBuffers,
    Uint32 bindingCount);
```

## Function Parameters

|                                          |                    |                                                       |
| ---------------------------------------- | ------------------ | ----------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **renderPass**     | a render pass handle.                                 |
| Uint32                                   | **firstSlot**      | the vertex storage buffer slot to begin binding from. |
| [SDL_GPUBuffer](SDL_GPUBuffer) *const *  | **storageBuffers** | an array of buffers.                                  |
| Uint32                                   | **bindingCount**   | the number of buffers to bind from the array.         |

## Remarks

These buffers must have been created with
[SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ](SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

