###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUIndexElementSize

Specifies the size of elements in an index buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUIndexElementSize
{
    SDL_GPU_INDEXELEMENTSIZE_16BIT, /**< The index elements are 16-bit. */
    SDL_GPU_INDEXELEMENTSIZE_32BIT  /**< The index elements are 32-bit. */
} SDL_GPUIndexElementSize;
```

## Version

This enum is available since SDL 3.1.3

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

