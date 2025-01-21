###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BindGPUFragmentStorageBuffers

Binds storage buffers for use on the fragment shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUFragmentStorageBuffers(
    SDL_GPURenderPass *render_pass,
    Uint32 first_slot,
    SDL_GPUBuffer *const *storage_buffers,
    Uint32 num_bindings);
```

## Function Parameters

|                                          |                     |                                                         |
| ---------------------------------------- | ------------------- | ------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass**     | a render pass handle.                                   |
| [Uint32](Uint32)                         | **first_slot**      | the fragment storage buffer slot to begin binding from. |
| [SDL_GPUBuffer](SDL_GPUBuffer) *const *  | **storage_buffers** | an array of storage buffers.                            |
| [Uint32](Uint32)                         | **num_bindings**    | the number of storage buffers to bind from the array.   |

## Remarks

These buffers must have been created with
[SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ](SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ).

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

