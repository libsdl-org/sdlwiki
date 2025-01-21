###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUVertexBufferDescription

A structure specifying the parameters of vertex buffers used in a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexBufferDescription
{
    Uint32 slot;                        /**< The binding slot of the vertex buffer. */
    Uint32 pitch;                       /**< The byte pitch between consecutive elements of the vertex buffer. */
    SDL_GPUVertexInputRate input_rate;  /**< Whether attribute addressing is a function of the vertex index or instance index. */
    Uint32 instance_step_rate;          /**< The number of instances to draw using the same per-instance data before advancing in the instance buffer by one element. Ignored unless input_rate is SDL_GPU_VERTEXINPUTRATE_INSTANCE */
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
- [SDL_GPUVertexInputState](SDL_GPUVertexInputState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

