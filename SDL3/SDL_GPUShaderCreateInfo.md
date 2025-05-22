# SDL_GPUShaderCreateInfo

A structure specifying code and metadata for creating a shader object.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUShaderCreateInfo
{
    size_t code_size;             /**< The size in bytes of the code pointed to. */
    const Uint8 *code;            /**< A pointer to shader code. */
    const char *entrypoint;       /**< A pointer to a null-terminated UTF-8 string specifying the entry point function name for the shader. */
    SDL_GPUShaderFormat format;   /**< The format of the shader code. */
    SDL_GPUShaderStage stage;     /**< The stage the shader program corresponds to. */
    Uint32 num_samplers;          /**< The number of samplers defined in the shader. */
    Uint32 num_storage_textures;  /**< The number of storage textures defined in the shader. */
    Uint32 num_storage_buffers;   /**< The number of storage buffers defined in the shader. */
    Uint32 num_uniform_buffers;   /**< The number of uniform buffers defined in the shader. */

    SDL_PropertiesID props;       /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUShaderCreateInfo;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUShader](SDL_CreateGPUShader)
- [SDL_GPUShaderFormat](SDL_GPUShaderFormat)
- [SDL_GPUShaderStage](SDL_GPUShaderStage)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

