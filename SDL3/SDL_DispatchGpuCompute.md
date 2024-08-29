###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DispatchGpuCompute

Dispatches compute work.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DispatchGpuCompute(
    SDL_GpuComputePass *computePass,
    Uint32 groupCountX,
    Uint32 groupCountY,
    Uint32 groupCountZ);
```

## Function Parameters

|                                            |                 |                                                            |
| ------------------------------------------ | --------------- | ---------------------------------------------------------- |
| [SDL_GpuComputePass](SDL_GpuComputePass) * | **computePass** | a compute pass handle.                                     |
| Uint32                                     | **groupCountX** | number of local workgroups to dispatch in the X dimension. |
| Uint32                                     | **groupCountY** | number of local workgroups to dispatch in the Y dimension. |
| Uint32                                     | **groupCountZ** | number of local workgroups to dispatch in the Z dimension. |

## Remarks

You must not call this function before binding a compute pipeline.

A VERY IMPORTANT NOTE If you dispatch multiple times in a compute pass, and
the dispatches write to the same resource region as each other, there is no
guarantee of which order the writes will occur. If the write order matters,
you MUST end the compute pass and begin another one.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


