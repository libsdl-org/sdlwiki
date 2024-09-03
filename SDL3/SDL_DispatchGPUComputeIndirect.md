###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DispatchGPUComputeIndirect

Dispatches compute work with parameters set from a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DispatchGPUComputeIndirect(
    SDL_GPUComputePass *computePass,
    SDL_GPUBuffer *buffer,
    Uint32 offsetInBytes);
```

## Function Parameters

|                                            |                   |                                                       |
| ------------------------------------------ | ----------------- | ----------------------------------------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) * | **computePass**   | a compute pass handle.                                |
| [SDL_GPUBuffer](SDL_GPUBuffer) *           | **buffer**        | a buffer containing dispatch parameters.              |
| Uint32                                     | **offsetInBytes** | the offset to start reading from the dispatch buffer. |

## Remarks

The buffer layout should match the layout of
[SDL_GPUIndirectDispatchCommand](SDL_GPUIndirectDispatchCommand). You must
not call this function before binding a compute pipeline.

A VERY IMPORTANT NOTE If you dispatch multiple times in a compute pass, and
the dispatches write to the same resource region as each other, there is no
guarantee of which order the writes will occur. If the write order matters,
you MUST end the compute pass and begin another one.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)
