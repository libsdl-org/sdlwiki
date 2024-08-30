###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireGPUCommandBuffer

Acquire a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUCommandBuffer* SDL_AcquireGPUCommandBuffer(
    SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context. |

## Return Value

([SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) *) Returns a command buffer.

## Remarks

This command buffer is managed by the implementation and should not be
freed by the user. The command buffer may only be used on the thread it was
acquired on. The command buffer should be submitted on the thread it was
acquired on.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

