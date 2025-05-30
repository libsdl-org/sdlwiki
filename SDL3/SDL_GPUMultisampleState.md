# SDL_GPUMultisampleState

A structure specifying the parameters of the graphics pipeline multisample state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUMultisampleState
{
    SDL_GPUSampleCount sample_count;  /**< The number of samples to be used in rasterization. */
    Uint32 sample_mask;               /**< Reserved for future use. Must be set to 0. */
    bool enable_mask;                 /**< Reserved for future use. Must be set to false. */
    bool enable_alpha_to_coverage;    /**< true enables the alpha-to-coverage feature. */
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUMultisampleState;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

