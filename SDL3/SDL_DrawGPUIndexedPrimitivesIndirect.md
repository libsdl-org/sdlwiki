###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DrawGPUIndexedPrimitivesIndirect

Draws data using bound graphics state with an index buffer enabled and with draw parameters set from a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DrawGPUIndexedPrimitivesIndirect(
    SDL_GPURenderPass *render_pass,
    SDL_GPUBuffer *buffer,
    Uint32 offset,
    Uint32 draw_count);
```

## Function Parameters

|                                          |                 |                                                                             |
| ---------------------------------------- | --------------- | --------------------------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass** | a render pass handle.                                                       |
| [SDL_GPUBuffer](SDL_GPUBuffer) *         | **buffer**      | a buffer containing draw parameters.                                        |
| Uint32                                   | **offset**      | the offset to start reading from the draw buffer.                           |
| Uint32                                   | **draw_count**  | the number of draw parameter sets that should be read from the draw buffer. |

## Remarks

The buffer must consist of tightly-packed draw parameter sets that each
match the layout of
[SDL_GPUIndexedIndirectDrawCommand](SDL_GPUIndexedIndirectDrawCommand). You
must not call this function before binding a graphics pipeline.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

