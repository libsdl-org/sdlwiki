# SDL_GPUColorTargetDescription

A structure specifying the parameters of color targets used in a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUColorTargetDescription
{
    SDL_GPUTextureFormat format;               /**< The pixel format of the texture to be used as a color target. */
    SDL_GPUColorTargetBlendState blend_state;  /**< The blend state to be used for the color target. */
} SDL_GPUColorTargetDescription;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GPUGraphicsPipelineTargetInfo](SDL_GPUGraphicsPipelineTargetInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

