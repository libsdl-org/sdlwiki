###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DrawGpuPrimitivesIndirect

Draws data using bound graphics state and with draw parameters set from a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DrawGpuPrimitivesIndirect(
    SDL_GpuRenderPass *renderPass,
    SDL_GpuBuffer *buffer,
    Uint32 offsetInBytes,
    Uint32 drawCount,
    Uint32 stride);
```

## Function Parameters

|                                          |                   |                                                                             |
| ---------------------------------------- | ----------------- | --------------------------------------------------------------------------- |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) * | **renderPass**    | a render pass handle.                                                       |
| [SDL_GpuBuffer](SDL_GpuBuffer) *         | **buffer**        | a buffer containing draw parameters.                                        |
| Uint32                                   | **offsetInBytes** | the offset to start reading from the draw buffer.                           |
| Uint32                                   | **drawCount**     | the number of draw parameter sets that should be read from the draw buffer. |
| Uint32                                   | **stride**        | the byte stride between sets of draw parameters.                            |

## Remarks

The buffer layout should match the layout of
[SDL_GpuIndirectDrawCommand](SDL_GpuIndirectDrawCommand). You must not call
this function before binding a graphics pipeline.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

