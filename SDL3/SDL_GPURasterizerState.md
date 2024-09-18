###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPURasterizerState

A structure specifying the parameters of the graphics pipeline rasterizer state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPURasterizerState
{
    SDL_GPUFillMode fill_mode;         /**< Whether polygons will be filled in or drawn as lines. */
    SDL_GPUCullMode cull_mode;         /**< The facing direction in which triangles will be culled. */
    SDL_GPUFrontFace front_face;       /**< The vertex winding that will cause a triangle to be determined as front-facing. */
    float depth_bias_constant_factor;  /**< A scalar factor controlling the depth value added to each fragment. */
    float depth_bias_clamp;            /**< The maximum depth bias of a fragment. */
    float depth_bias_slope_factor;     /**< A scalar factor applied to a fragment's slope in depth calculations. */
    bool enable_depth_bias;        /**< true to bias fragment depth values. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPURasterizerState;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

