###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SubmitGpu

Submits a command buffer so its commands can be processed on the GPU.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SubmitGpu(
    SDL_GpuCommandBuffer *commandBuffer);
```

## Function Parameters

|                                                |                   |                   |
| ---------------------------------------------- | ----------------- | ----------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer. |

## Remarks

It is invalid to use the command buffer after this is called.

This must be called from the thread the command buffer was acquired on.

All commands in the submission are guaranteed to begin executing before any
command in a subsequent submission begins executing.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AcquireGpuCommandBuffer](SDL_AcquireGpuCommandBuffer)
- [SDL_AcquireGpuSwapchainTexture](SDL_AcquireGpuSwapchainTexture)
- [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

