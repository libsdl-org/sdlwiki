###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUVertexBinding

A structure specifying a vertex binding.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexBinding
{
    Uint32 index;                     /**< The binding index. */
    Uint32 pitch;                       /**< The byte pitch between consecutive elements of the vertex buffer. */
    SDL_GPUVertexInputRate input_rate;  /**< Whether attribute addressing is a function of the vertex index or instance index. */
    Uint32 instance_step_rate;          /**< The number of instances to draw using the same per-instance data before advancing in the instance buffer by one element. Ignored unless input_rate is SDL_GPU_VERTEXINPUTRATE_INSTANCE */
} SDL_GPUVertexBinding;
```

## Remarks

When you call [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers), you
specify the binding indices of the vertex buffers. For example if you
called [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers) with a
first_binding of 2 and num_bindings of 3, the binding indices 2, 3, 4 would
be used by the vertex buffers you pass in.

Vertex attributes are linked to bindings via the index. The binding_index
field of [SDL_GPUVertexAttribute](SDL_GPUVertexAttribute) specifies the
vertex buffer binding index that the attribute will be read from.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUVertexAttribute](SDL_GPUVertexAttribute)
- [SDL_GPUVertexInputState](SDL_GPUVertexInputState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

