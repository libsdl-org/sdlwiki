# SDL_DrawGPUPrimitives

Draws data using bound graphics state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DrawGPUPrimitives(
    SDL_GPURenderPass *render_pass,
    Uint32 num_vertices,
    Uint32 num_instances,
    Uint32 first_vertex,
    Uint32 first_instance);
```

## Function Parameters

|                                          |                    |                                             |
| ---------------------------------------- | ------------------ | ------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass**    | a render pass handle.                       |
| [Uint32](Uint32)                         | **num_vertices**   | the number of vertices to draw.             |
| [Uint32](Uint32)                         | **num_instances**  | the number of instances that will be drawn. |
| [Uint32](Uint32)                         | **first_vertex**   | the index of the first vertex to draw.      |
| [Uint32](Uint32)                         | **first_instance** | the ID of the first instance to draw.       |

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





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

