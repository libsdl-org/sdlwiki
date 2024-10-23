###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUPrimitiveType

Specifies the primitive topology of a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUPrimitiveType
{
    SDL_GPU_PRIMITIVETYPE_TRIANGLELIST,  /**< A series of separate triangles. */
    SDL_GPU_PRIMITIVETYPE_TRIANGLESTRIP, /**< A series of connected triangles. */
    SDL_GPU_PRIMITIVETYPE_LINELIST,      /**< A series of separate lines. */
    SDL_GPU_PRIMITIVETYPE_LINESTRIP,     /**< A series of connected lines. */
    SDL_GPU_PRIMITIVETYPE_POINTLIST      /**< A series of separate points. */
} SDL_GPUPrimitiveType;
```

## Version

This enum is available since SDL 3.1.3

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

