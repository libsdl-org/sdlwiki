###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUMultisampleState

A structure specifying the parameters of the graphics pipeline multisample state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUMultisampleState
{
    SDL_GPUSampleCount sample_count;  /**< The number of samples to be used in rasterization. */
    Uint32 sample_mask;               /**< Determines which samples get updated in the render targets. Treated as 0xFFFFFFFF if enable_mask is false. */
    bool enable_mask;             /**< Enables sample masking. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUMultisampleState;
```

## Version

This struct is available since SDL 3.2.0

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

