###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUVertexAttribute

A structure specifying a vertex attribute.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVertexAttribute
{
    Uint32 location;                    /**< The shader input location index. */
    Uint32 buffer_slot;                 /**< The binding slot of the associated vertex buffer. */
    SDL_GPUVertexElementFormat format;  /**< The size and type of the attribute data. */
    Uint32 offset;                      /**< The byte offset of this attribute relative to the start of the vertex element. */
} SDL_GPUVertexAttribute;
```

## Remarks

All vertex attribute locations provided to an
[SDL_GPUVertexInputState](SDL_GPUVertexInputState) must be unique.

## Version

This struct is available since SDL 3.2.0

## See Also

- [SDL_GPUVertexBufferDescription](SDL_GPUVertexBufferDescription)
- [SDL_GPUVertexInputState](SDL_GPUVertexInputState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

