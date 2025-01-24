# SDL_GPUStencilOpState

A structure specifying the stencil operation state of a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUStencilOpState
{
    SDL_GPUStencilOp fail_op;        /**< The action performed on samples that fail the stencil test. */
    SDL_GPUStencilOp pass_op;        /**< The action performed on samples that pass the depth and stencil tests. */
    SDL_GPUStencilOp depth_fail_op;  /**< The action performed on samples that pass the stencil test and fail the depth test. */
    SDL_GPUCompareOp compare_op;     /**< The comparison operator used in the stencil test. */
} SDL_GPUStencilOpState;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GPUDepthStencilState](SDL_GPUDepthStencilState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

