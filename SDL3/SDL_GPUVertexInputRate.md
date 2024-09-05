###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUVertexInputRate

Specifies the rate at which vertex attributes are pulled from buffers.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUVertexInputRate
{
    SDL_GPU_VERTEXINPUTRATE_VERTEX = 0,   /**< Attribute addressing is a function of the vertex index. */
    SDL_GPU_VERTEXINPUTRATE_INSTANCE = 1  /**< Attribute addressing is a function of the instance index. */
} SDL_GPUVertexInputRate;
```

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

