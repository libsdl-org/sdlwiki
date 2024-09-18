###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUStorageBufferWriteOnlyBinding

A structure specifying parameters related to binding buffers in a compute pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUStorageBufferWriteOnlyBinding
{
    SDL_GPUBuffer *buffer;  /**< The buffer to bind. Must have been created with SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE. */
    bool cycle;         /**< true cycles the buffer if it is already bound. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUStorageBufferWriteOnlyBinding;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_BeginGPUComputePass](SDL_BeginGPUComputePass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

