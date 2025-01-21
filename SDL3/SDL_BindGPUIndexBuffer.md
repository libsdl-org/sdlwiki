###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BindGPUIndexBuffer

Binds an index buffer on a command buffer for use with subsequent draw calls.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUIndexBuffer(
    SDL_GPURenderPass *render_pass,
    const SDL_GPUBufferBinding *binding,
    SDL_GPUIndexElementSize index_element_size);
```

## Function Parameters

|                                                      |                        |                                                              |
| ---------------------------------------------------- | ---------------------- | ------------------------------------------------------------ |
| [SDL_GPURenderPass](SDL_GPURenderPass) *             | **render_pass**        | a render pass handle.                                        |
| const [SDL_GPUBufferBinding](SDL_GPUBufferBinding) * | **binding**            | a pointer to a struct containing an index buffer and offset. |
| [SDL_GPUIndexElementSize](SDL_GPUIndexElementSize)   | **index_element_size** | whether the index values in the buffer are 16- or 32-bit.    |

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

