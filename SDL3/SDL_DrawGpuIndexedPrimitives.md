###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DrawGpuIndexedPrimitives

Draws data using bound graphics state with an index buffer and instancing enabled.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DrawGpuIndexedPrimitives(
    SDL_GpuRenderPass *renderPass,
    Uint32 indexCount,
    Uint32 instanceCount,
    Uint32 firstIndex,
    Sint32 vertexOffset,
    Uint32 firstInstance);
```

## Function Parameters

|                                          |                   |                                                                     |
| ---------------------------------------- | ----------------- | ------------------------------------------------------------------- |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) * | **renderPass**    | a render pass handle.                                               |
| Uint32                                   | **indexCount**    | the number of vertices to draw per instance.                        |
| Uint32                                   | **instanceCount** | the number of instances to draw.                                    |
| Uint32                                   | **firstIndex**    | the starting index within the index buffer.                         |
| Sint32                                   | **vertexOffset**  | value added to vertex index before indexing into the vertex buffer. |
| Uint32                                   | **firstInstance** | the ID of the first instance to draw.                               |

## Remarks

You must not call this function before binding a graphics pipeline.

Note that the `firstVertex` and `firstInstance` parameters are NOT
compatible with built-in vertex/instance ID variables in shaders (for
example, SV_VertexID). If your shader depends on these variables, the
correlating draw call parameter MUST be 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


