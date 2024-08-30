###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUVertexBuffers

Binds vertex buffers on a command buffer for use with subsequent draw calls.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUVertexBuffers(
    SDL_GPURenderPass *renderPass,
    Uint32 firstBinding,
    SDL_GPUBufferBinding *pBindings,
    Uint32 bindingCount);
```

## Function Parameters

|                                                |                  |                                                                                                               |
| ---------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) *       | **renderPass**   | a render pass handle.                                                                                         |
| Uint32                                         | **firstBinding** | the starting bind point for the vertex buffers.                                                               |
| [SDL_GPUBufferBinding](SDL_GPUBufferBinding) * | **pBindings**    | an array of [SDL_GPUBufferBinding](SDL_GPUBufferBinding) structs containing vertex buffers and offset values. |
| Uint32                                         | **bindingCount** | the number of bindings in the pBindings array.                                                                |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

