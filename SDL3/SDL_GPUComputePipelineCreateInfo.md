###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUComputePipelineCreateInfo

A structure specifying the parameters of a compute pipeline state.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUComputePipelineCreateInfo
{
    size_t code_size;                       /**< The size in bytes of the compute shader code pointed to. */
    const Uint8 *code;                      /**< A pointer to compute shader code. */
    const char *entrypoint;                 /**< A pointer to a null-terminated UTF-8 string specifying the entry point function name for the shader. */
    SDL_GPUShaderFormat format;             /**< The format of the compute shader code. */
    Uint32 num_samplers;                    /**< The number of samplers defined in the shader. */
    Uint32 num_readonly_storage_textures;   /**< The number of readonly storage textures defined in the shader. */
    Uint32 num_readonly_storage_buffers;    /**< The number of readonly storage buffers defined in the shader. */
    Uint32 num_readwrite_storage_textures;  /**< The number of read-write storage textures defined in the shader. */
    Uint32 num_readwrite_storage_buffers;   /**< The number of read-write storage buffers defined in the shader. */
    Uint32 num_uniform_buffers;             /**< The number of uniform buffers defined in the shader. */
    Uint32 threadcount_x;                   /**< The number of threads in the X dimension. This should match the value in the shader. */
    Uint32 threadcount_y;                   /**< The number of threads in the Y dimension. This should match the value in the shader. */
    Uint32 threadcount_z;                   /**< The number of threads in the Z dimension. This should match the value in the shader. */

    SDL_PropertiesID props;                 /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUComputePipelineCreateInfo;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUComputePipeline](SDL_CreateGPUComputePipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

