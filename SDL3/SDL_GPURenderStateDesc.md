# SDL_GPURenderStateDesc

GPU render state description.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
typedef struct SDL_GPURenderStateDesc
{
    Uint32 version;                 /**< the version of this interface */

    SDL_GPUShader *fragment_shader; /**< The fragment shader to use when this render state is active */

    Sint32 num_sampler_bindings;    /**< The number of additional fragment samplers to bind when this render state is active */
    const SDL_GPUTextureSamplerBinding *sampler_bindings;   /**< Additional fragment samplers to bind when this render state is active */

    Sint32 num_storage_textures;    /**< The number of storage textures to bind when this render state is active */
    SDL_GPUTexture *const *storage_textures;    /**< Storage textures to bind when this render state is active */

    Sint32 num_storage_buffers;    /**< The number of storage buffers to bind when this render state is active */
    SDL_GPUBuffer *const *storage_buffers;      /**< Storage buffers to bind when this render state is active */
} SDL_GPURenderStateDesc;
```

## Remarks

This structure should be initialized using
[SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)().

## Version

This struct is available since SDL 3.4.0.

## See Also

- [SDL_CreateGPURenderState](SDL_CreateGPURenderState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRender](CategoryRender)

