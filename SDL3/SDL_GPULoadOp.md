###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPULoadOp

Specifies how the contents of a texture attached to a render pass are treated at the beginning of the render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPULoadOp
{
    SDL_GPU_LOADOP_LOAD,      /**< The previous contents of the texture will be preserved. */
    SDL_GPU_LOADOP_CLEAR,     /**< The contents of the texture will be cleared to a color. */
    SDL_GPU_LOADOP_DONT_CARE  /**< The previous contents of the texture need not be preserved. The contents will be undefined. */
} SDL_GPULoadOp;
```

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

