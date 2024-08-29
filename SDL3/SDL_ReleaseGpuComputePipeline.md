###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseGpuComputePipeline

Frees the given compute pipeline as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGpuComputePipeline(
    SDL_GpuDevice *device,
    SDL_GpuComputePipeline *computePipeline);
```

## Function Parameters

|                                                    |                     |                                     |
| -------------------------------------------------- | ------------------- | ----------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                   | **device**          | a GPU context.                      |
| [SDL_GpuComputePipeline](SDL_GpuComputePipeline) * | **computePipeline** | a compute pipeline to be destroyed. |

## Remarks

You must not reference the compute pipeline after calling this function.

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

