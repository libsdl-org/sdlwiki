###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BindGPUVertexBuffers

Binds vertex buffers on a command buffer for use with subsequent draw calls.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUVertexBuffers(
    SDL_GPURenderPass *render_pass,
    Uint32 first_slot,
    const SDL_GPUBufferBinding *bindings,
    Uint32 num_bindings);
```

## Function Parameters

|                                                      |                  |                                                                                                               |
| ---------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) *             | **render_pass**  | a render pass handle.                                                                                         |
| Uint32                                               | **first_slot**   | the vertex buffer slot to begin binding from.                                                                 |
| const [SDL_GPUBufferBinding](SDL_GPUBufferBinding) * | **bindings**     | an array of [SDL_GPUBufferBinding](SDL_GPUBufferBinding) structs containing vertex buffers and offset values. |
| Uint32                                               | **num_bindings** | the number of bindings in the bindings array.                                                                 |

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

