###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGpuIndexBuffer

Binds an index buffer on a command buffer for use with subsequent draw calls.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGpuIndexBuffer(
    SDL_GpuRenderPass *renderPass,
    SDL_GpuBufferBinding *pBinding,
    SDL_GpuIndexElementSize indexElementSize);
```

## Function Parameters

|                                                    |                      |                                                              |
| -------------------------------------------------- | -------------------- | ------------------------------------------------------------ |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) *           | **renderPass**       | a render pass handle.                                        |
| [SDL_GpuBufferBinding](SDL_GpuBufferBinding) *     | **pBinding**         | a pointer to a struct containing an index buffer and offset. |
| [SDL_GpuIndexElementSize](SDL_GpuIndexElementSize) | **indexElementSize** | whether the index values in the buffer are 16- or 32-bit.    |

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

