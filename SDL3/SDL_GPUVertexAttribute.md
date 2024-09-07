###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUVertexAttribute

A structure specifying a vertex attribute.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexAttribute
{
    Uint32 location;                    /**< The shader input location index. */
    Uint32 binding_index;               /**< The binding index. */
    SDL_GPUVertexElementFormat format;  /**< The size and type of the attribute data. */
    Uint32 offset;                      /**< The byte offset of this attribute relative to the start of the vertex element. */
} SDL_GPUVertexAttribute;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUVertexBinding](SDL_GPUVertexBinding)
- [SDL_GPUVertexInputState](SDL_GPUVertexInputState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

