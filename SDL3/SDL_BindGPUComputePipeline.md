# SDL_BindGPUComputePipeline

Binds a compute pipeline on a command buffer for use in compute dispatch.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUComputePipeline(
    SDL_GPUComputePass *compute_pass,
    SDL_GPUComputePipeline *compute_pipeline);
```

## Function Parameters

|                                                    |                      |                             |
| -------------------------------------------------- | -------------------- | --------------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) *         | **compute_pass**     | a compute pass handle.      |
| [SDL_GPUComputePipeline](SDL_GPUComputePipeline) * | **compute_pipeline** | a compute pipeline to bind. |

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

