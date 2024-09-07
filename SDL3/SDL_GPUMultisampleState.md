###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUMultisampleState

A structure specifying the parameters of the graphics pipeline multisample state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUMultisampleState
{
    SDL_GPUSampleCount sample_count;  /**< The number of samples to be used in rasterization. */
    Uint32 sample_mask;               /**< Determines which samples get updated in the render targets. 0xFFFFFFFF is a reasonable default. */
} SDL_GPUMultisampleState;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

