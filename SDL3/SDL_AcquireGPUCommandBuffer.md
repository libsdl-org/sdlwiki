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

([SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) *) Returns a command buffer,
or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This command buffer is managed by the implementation and should not be
freed by the user. The command buffer may only be used on the thread it was
acquired on. The command buffer should be submitted on the thread it was
acquired on.

It is valid to acquire multiple command buffers on the same thread at once.
In fact a common design pattern is to acquire two command buffers per frame
where one is dedicated to render and compute passes and the other is
dedicated to copy passes and other preparatory work such as generating
mipmaps. Interleaving commands between the two command buffers reduces the
total amount of passes overall which improves rendering performance.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

