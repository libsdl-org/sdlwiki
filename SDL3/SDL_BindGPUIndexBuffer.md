###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUIndexBuffer

Binds an index buffer on a command buffer for use with subsequent draw calls.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUIndexBuffer(
    SDL_GPURenderPass *renderPass,
    SDL_GPUBufferBinding *pBinding,
    SDL_GPUIndexElementSize indexElementSize);
```

## Function Parameters

|                                                    |                      |                                                              |
| -------------------------------------------------- | -------------------- | ------------------------------------------------------------ |
| [SDL_GPURenderPass](SDL_GPURenderPass) *           | **renderPass**       | a render pass handle.                                        |
| [SDL_GPUBufferBinding](SDL_GPUBufferBinding) *     | **pBinding**         | a pointer to a struct containing an index buffer and offset. |
| [SDL_GPUIndexElementSize](SDL_GPUIndexElementSize) | **indexElementSize** | whether the index values in the buffer are 16- or 32-bit.    |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

