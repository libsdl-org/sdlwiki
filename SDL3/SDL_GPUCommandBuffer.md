###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

In multi-threading scenarios, you should acquire and submit a command
buffer on the same thread. As long as you satisfy this requirement, all
functionality related to command buffers is thread-safe.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

