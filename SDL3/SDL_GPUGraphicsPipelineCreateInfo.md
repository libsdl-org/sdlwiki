###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUGraphicsPipelineCreateInfo

A structure specifying the parameters of a graphics pipeline state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUGraphicsPipelineCreateInfo
{
    SDL_GPUShader *vertex_shader;                   /**< The vertex shader used by the graphics pipeline. */
    SDL_GPUShader *fragment_shader;                 /**< The fragment shader used by the graphics pipeline. */
    SDL_GPUVertexInputState vertex_input_state;     /**< The vertex layout of the graphics pipeline. */
    SDL_GPUPrimitiveType primitive_type;            /**< The primitive topology of the graphics pipeline. */
    SDL_GPURasterizerState rasterizer_state;        /**< The rasterizer state of the graphics pipeline. */
    SDL_GPUMultisampleState multisample_state;      /**< The multisample state of the graphics pipeline. */
    SDL_GPUDepthStencilState depth_stencil_state;   /**< The depth-stencil state of the graphics pipeline. */
    SDL_GpuGraphicsPipelineTargetInfo target_info;  /**< Formats and blend modes for the render targets of the graphics pipeline. */

    SDL_PropertiesID props;                         /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUGraphicsPipelineCreateInfo;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

