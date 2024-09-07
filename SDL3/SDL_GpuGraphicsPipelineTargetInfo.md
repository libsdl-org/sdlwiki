###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GpuGraphicsPipelineTargetInfo

A structure specifying the descriptions of render targets used in a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GpuGraphicsPipelineTargetInfo
{
    const SDL_GPUColorTargetDescription *color_target_descriptions;  /**< A pointer to an array of color target descriptions. */
    Uint32 num_color_targets;                                        /**< The number of color target descriptions in the above array. */
    SDL_bool has_depth_stencil_target;                               /**< SDL_TRUE specifies that the pipeline uses a depth-stencil target. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    SDL_GPUTextureFormat depth_stencil_format;                       /**< The pixel format of the depth-stencil target. Ignored if has_depth_stencil_target is SDL_FALSE. */
} SDL_GpuGraphicsPipelineTargetInfo;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

