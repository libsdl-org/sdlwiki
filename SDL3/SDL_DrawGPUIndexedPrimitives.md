# SDL_DrawGPUIndexedPrimitives

Draws data using bound graphics state with an index buffer and instancing enabled.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DrawGPUIndexedPrimitives(
    SDL_GPURenderPass *render_pass,
    Uint32 num_indices,
    Uint32 num_instances,
    Uint32 first_index,
    Sint32 vertex_offset,
    Uint32 first_instance);
```

## Function Parameters

|                                          |                    |                                                                     |
| ---------------------------------------- | ------------------ | ------------------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass**    | a render pass handle.                                               |
| [Uint32](Uint32)                         | **num_indices**    | the number of indices to draw per instance.                         |
| [Uint32](Uint32)                         | **num_instances**  | the number of instances to draw.                                    |
| [Uint32](Uint32)                         | **first_index**    | the starting index within the index buffer.                         |
| [Sint32](Sint32)                         | **vertex_offset**  | value added to vertex index before indexing into the vertex buffer. |
| [Uint32](Uint32)                         | **first_instance** | the ID of the first instance to draw.                               |

## Remarks

You must not call this function before binding a graphics pipeline.

Note that the `first_vertex` and `first_instance` parameters are NOT
compatible with built-in vertex/instance ID variables in shaders (for
example, SV_VertexID); GPU APIs and shader languages do not define these
built-in variables consistently, so if your shader depends on them, the
only way to keep behavior consistent and portable is to always pass 0 for
the correlating parameter in the draw calls.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

