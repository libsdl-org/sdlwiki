# SDL_GPUIndexedIndirectDrawCommand

A structure specifying the parameters of an indexed indirect draw command.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUIndexedIndirectDrawCommand
{
    Uint32 num_indices;    /**< The number of indices to draw per instance. */
    Uint32 num_instances;  /**< The number of instances to draw. */
    Uint32 first_index;    /**< The base index within the index buffer. */
    Sint32 vertex_offset;  /**< The value added to the vertex index before indexing into the vertex buffer. */
    Uint32 first_instance; /**< The ID of the first instance to draw. */
} SDL_GPUIndexedIndirectDrawCommand;
```

## Remarks

Note that the `first_vertex` and `first_instance` parameters are NOT
compatible with built-in vertex/instance ID variables in shaders (for
example, SV_VertexID); GPU APIs and shader languages do not define these
built-in variables consistently, so if your shader depends on them, the
only way to keep behavior consistent and portable is to always pass 0 for
the correlating parameter in the draw calls.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_DrawGPUIndexedPrimitivesIndirect](SDL_DrawGPUIndexedPrimitivesIndirect)






----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

