###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUVertexInputState

A structure specifying the parameters of a graphics pipeline vertex input state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexInputState
{
    const SDL_GPUVertexBufferDescription *vertex_buffer_descriptions; /**< A pointer to an array of vertex buffer descriptions. */
    Uint32 num_vertex_buffers;                                        /**< The number of vertex buffer descriptions in the above array. */
    const SDL_GPUVertexAttribute *vertex_attributes;                  /**< A pointer to an array of vertex attribute descriptions. */
    Uint32 num_vertex_attributes;                                     /**< The number of vertex attribute descriptions in the above array. */
} SDL_GPUVertexInputState;
```

## Version

This struct is available since SDL 3.1.3

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)
- [SDL_GPUVertexBufferDescription](SDL_GPUVertexBufferDescription)
- [SDL_GPUVertexAttribute](SDL_GPUVertexAttribute)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

