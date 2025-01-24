# SDL_GPUDepthStencilTargetInfo

A structure specifying the parameters of a depth-stencil target used by a render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUDepthStencilTargetInfo
{
    SDL_GPUTexture *texture;               /**< The texture that will be used as the depth stencil target by the render pass. */
    float clear_depth;                     /**< The value to clear the depth component to at the beginning of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
    SDL_GPULoadOp load_op;                 /**< What is done with the depth contents at the beginning of the render pass. */
    SDL_GPUStoreOp store_op;               /**< What is done with the depth results of the render pass. */
    SDL_GPULoadOp stencil_load_op;         /**< What is done with the stencil contents at the beginning of the render pass. */
    SDL_GPUStoreOp stencil_store_op;       /**< What is done with the stencil results of the render pass. */
    bool cycle;                        /**< true cycles the texture if the texture is bound and any load ops are not LOAD */
    Uint8 clear_stencil;                   /**< The value to clear the stencil component to at the beginning of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
    Uint8 padding1;
    Uint8 padding2;
} SDL_GPUDepthStencilTargetInfo;
```

## Remarks

The load_op field determines what is done with the depth contents of the
texture at the beginning of the render pass.

- LOAD: Loads the depth values currently in the texture.
- CLEAR: Clears the texture to a single depth.
- DONT_CARE: The driver will do whatever it wants with the memory. This is
  a good option if you know that every single pixel will be touched in the
  render pass.

The store_op field determines what is done with the depth results of the
render pass.

- STORE: Stores the depth results in the texture.
- DONT_CARE: The driver will do whatever it wants with the depth results.
  This is often a good option for depth/stencil textures that don't need to
  be reused again.

The stencil_load_op field determines what is done with the stencil contents
of the texture at the beginning of the render pass.

- LOAD: Loads the stencil values currently in the texture.
- CLEAR: Clears the stencil values to a single value.
- DONT_CARE: The driver will do whatever it wants with the memory. This is
  a good option if you know that every single pixel will be touched in the
  render pass.

The stencil_store_op field determines what is done with the stencil results
of the render pass.

- STORE: Stores the stencil results in the texture.
- DONT_CARE: The driver will do whatever it wants with the stencil results.
  This is often a good option for depth/stencil textures that don't need to
  be reused again.

Note that depth/stencil targets do not support multisample resolves.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

