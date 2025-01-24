# SDL_GPUCullMode

Specifies the facing direction in which triangle faces will be culled.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUCullMode
{
    SDL_GPU_CULLMODE_NONE,   /**< No triangles are culled. */
    SDL_GPU_CULLMODE_FRONT,  /**< Front-facing triangles are culled. */
    SDL_GPU_CULLMODE_BACK    /**< Back-facing triangles are culled. */
} SDL_GPUCullMode;
```

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)






----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

