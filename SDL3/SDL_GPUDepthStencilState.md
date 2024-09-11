###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUDepthStencilState

A structure specifying the parameters of the graphics pipeline depth stencil state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUDepthStencilState
{
    SDL_GPUCompareOp compare_op;                /**< The comparison operator used for depth testing. */
    SDL_GPUStencilOpState back_stencil_state;   /**< The stencil op state for back-facing triangles. */
    SDL_GPUStencilOpState front_stencil_state;  /**< The stencil op state for front-facing triangles. */
    Uint8 compare_mask;                         /**< Selects the bits of the stencil values participating in the stencil test. */
    Uint8 write_mask;                           /**< Selects the bits of the stencil values updated by the stencil test. */
    SDL_bool enable_depth_test;                 /**< SDL_TRUE enables the depth test. */
    SDL_bool enable_depth_write;                /**< SDL_TRUE enables depth writes. Depth writes are always disabled when enable_depth_test is SDL_FALSE. */
    SDL_bool enable_stencil_test;               /**< SDL_TRUE enables the stencil test. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUDepthStencilState;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

