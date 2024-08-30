###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SubmitGPUAndAcquireFence

Submits a command buffer so its commands can be processed on the GPU, and acquires a fence associated with the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUFence* SDL_SubmitGPUAndAcquireFence(
    SDL_GPUCommandBuffer *commandBuffer);
```

## Function Parameters

|                                                |                   |                   |
| ---------------------------------------------- | ----------------- | ----------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **commandBuffer** | a command buffer. |

## Return Value

([SDL_GPUFence](SDL_GPUFence) *) Returns a fence associated with the
command buffer.

## Remarks

You must release this fence when it is no longer needed or it will cause a
leak. It is invalid to use the command buffer after this is called.

This must be called from the thread the command buffer was acquired on.

All commands in the submission are guaranteed to begin executing before any
command in a subsequent submission begins executing.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)
- [SDL_SubmitGPU](SDL_SubmitGPU)
- [SDL_ReleaseGPUFence](SDL_ReleaseGPUFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

