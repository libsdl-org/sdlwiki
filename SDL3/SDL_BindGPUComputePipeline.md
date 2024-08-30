###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUComputePipeline

Binds a compute pipeline on a command buffer for use in compute dispatch.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUComputePipeline(
    SDL_GPUComputePass *computePass,
    SDL_GPUComputePipeline *computePipeline);
```

## Function Parameters

|                                                    |                     |                             |
| -------------------------------------------------- | ------------------- | --------------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) *         | **computePass**     | a compute pass handle.      |
| [SDL_GPUComputePipeline](SDL_GPUComputePipeline) * | **computePipeline** | a compute pipeline to bind. |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

