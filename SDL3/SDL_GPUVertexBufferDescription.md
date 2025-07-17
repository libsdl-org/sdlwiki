# SDL_GPUVertexBufferDescription

A structure specifying the parameters of vertex buffers used in a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexBufferDescription
{
    Uint32 slot;                        /**< The binding slot of the vertex buffer. */
    Uint32 pitch;                       /**< The size of a single element + the offset between elements. */
    SDL_GPUVertexInputRate input_rate;  /**< Whether attribute addressing is a function of the vertex index or instance index. */
    Uint32 instance_step_rate;          /**< Reserved for future use. Must be set to 0. */
} SDL_GPUVertexBufferDescription;
```

## Remarks

When you call [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers), you
specify the binding slots of the vertex buffers. For example if you called
[SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers) with a first_slot of 2
and num_bindings of 3, the binding slots 2, 3, 4 would be used by the
vertex buffers you pass in.

Vertex attributes are linked to buffers via the buffer_slot field of
[SDL_GPUVertexAttribute](SDL_GPUVertexAttribute). For example, if an
attribute has a buffer_slot of 0, then that attribute belongs to the vertex
buffer bound at slot 0.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GPUVertexAttribute](SDL_GPUVertexAttribute)
- [SDL_GPUVertexInputRate](SDL_GPUVertexInputRate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

