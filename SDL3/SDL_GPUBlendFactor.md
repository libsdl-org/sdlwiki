# SDL_GPUBlendFactor

Specifies a blending factor to be used when pixels in a render target are blended with existing pixels in the texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUBlendFactor
{
    SDL_GPU_BLENDFACTOR_INVALID,
    SDL_GPU_BLENDFACTOR_ZERO,                      /**< 0 */
    SDL_GPU_BLENDFACTOR_ONE,                       /**< 1 */
    SDL_GPU_BLENDFACTOR_SRC_COLOR,                 /**< source color */
    SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_COLOR,       /**< 1 - source color */
    SDL_GPU_BLENDFACTOR_DST_COLOR,                 /**< destination color */
    SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_COLOR,       /**< 1 - destination color */
    SDL_GPU_BLENDFACTOR_SRC_ALPHA,                 /**< source alpha */
    SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_ALPHA,       /**< 1 - source alpha */
    SDL_GPU_BLENDFACTOR_DST_ALPHA,                 /**< destination alpha */
    SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_ALPHA,       /**< 1 - destination alpha */
    SDL_GPU_BLENDFACTOR_CONSTANT_COLOR,            /**< blend constant */
    SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR,  /**< 1 - blend constant */
    SDL_GPU_BLENDFACTOR_SRC_ALPHA_SATURATE         /**< min(source alpha, 1 - destination alpha) */
} SDL_GPUBlendFactor;
```

## Remarks

The source color is the value written by the fragment shader. The
destination color is the value currently existing in the texture.

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)






----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

