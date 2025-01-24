# SDL_GPUPrimitiveType

Specifies the primitive topology of a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUPrimitiveType
{
    SDL_GPU_PRIMITIVETYPE_TRIANGLELIST,  /**< A series of separate triangles. */
    SDL_GPU_PRIMITIVETYPE_TRIANGLESTRIP, /**< A series of connected triangles. */
    SDL_GPU_PRIMITIVETYPE_LINELIST,      /**< A series of separate lines. */
    SDL_GPU_PRIMITIVETYPE_LINESTRIP,     /**< A series of connected lines. */
    SDL_GPU_PRIMITIVETYPE_POINTLIST      /**< A series of separate points. */
} SDL_GPUPrimitiveType;
```

## Remarks

If you are using POINTLIST you must include a point size output in the
vertex shader.

- For HLSL compiling to SPIRV you must decorate a float output with
  [[vk::builtin("PointSize")]].
- For GLSL you must set the gl_PointSize builtin.
- For MSL you must include a float output with the [[point_size]]
  decorator.

Note that sized point topology is totally unsupported on D3D12. Any size
other than 1 will be ignored. In general, you should avoid using point
topology for both compatibility and performance reasons. You WILL regret
using it.

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)






----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

