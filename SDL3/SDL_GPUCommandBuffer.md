# SDL_GPUCommandBuffer

An opaque handle representing a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUCommandBuffer SDL_GPUCommandBuffer;
```

## Remarks

Most state is managed via command buffers. When setting state using a
command buffer, that state is local to the command buffer.

Commands only begin execution on the GPU once
[SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer) is called. Once
the command buffer is submitted, it is no longer valid to use it.

Command buffers are executed in submission order. If you submit command
buffer A and then command buffer B all commands in A will begin executing
before any command in B begins executing.

In multi-threading scenarios, you should only access a command buffer on
the thread you acquired it from.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

