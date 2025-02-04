# SDL_SubmitGPUCommandBufferAndAcquireFence

Submits a command buffer so its commands can be processed on the GPU, and acquires a fence associated with the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUFence * SDL_SubmitGPUCommandBufferAndAcquireFence(
    SDL_GPUCommandBuffer *command_buffer);
```

## Function Parameters

|                                                |                    |                   |
| ---------------------------------------------- | ------------------ | ----------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer. |

## Return Value

([SDL_GPUFence](SDL_GPUFence) *) Returns a fence associated with the
command buffer, or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

You must release this fence when it is no longer needed or it will cause a
leak. It is invalid to use the command buffer after this is called.

This must be called from the thread the command buffer was acquired on.

All commands in the submission are guaranteed to begin executing before any
command in a subsequent submission begins executing.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_ReleaseGPUFence](SDL_ReleaseGPUFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

