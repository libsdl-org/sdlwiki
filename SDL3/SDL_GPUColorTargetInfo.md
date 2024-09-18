###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUColorTargetInfo

A structure specifying the parameters of a color target used by a render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUColorTargetInfo
{
    SDL_GPUTexture *texture;         /**< The texture that will be used as a color target by a render pass. */
    Uint32 mip_level;                /**< The mip level to use as a color target. */
    Uint32 layer_or_depth_plane;     /**< The layer index or depth plane to use as a color target. This value is treated as a layer index on 2D array and cube textures, and as a depth plane on 3D textures. */
    SDL_FColor clear_color;          /**< The color to clear the color target to at the start of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
    SDL_GPULoadOp load_op;           /**< What is done with the contents of the color target at the beginning of the render pass. */
    SDL_GPUStoreOp store_op;         /**< What is done with the results of the render pass. */
    SDL_GPUTexture *resolve_texture; /**< The texture that will receive the results of a multisample resolve operation. Ignored if a RESOLVE* store_op is not used. */
    Uint32 resolve_mip_level;        /**< The mip level of the resolve texture to use for the resolve operation. Ignored if a RESOLVE* store_op is not used. */
    Uint32 resolve_layer;            /**< The layer index of the resolve texture to use for the resolve operation. Ignored if a RESOLVE* store_op is not used. */
    bool cycle;                  /**< true cycles the texture if the texture is bound and load_op is not LOAD */
    bool cycle_resolve_texture;  /**< true cycles the resolve texture if the resolve texture is bound. Ignored if a RESOLVE* store_op is not used. */
    Uint8 padding1;
    Uint8 padding2;
} SDL_GPUColorTargetInfo;
```

## Remarks

The load_op field determines what is done with the texture at the beginning
of the render pass.

- LOAD: Loads the data currently in the texture. Not recommended for
  multisample textures as it requires significant memory bandwidth.
- CLEAR: Clears the texture to a single color.
- DONT_CARE: The driver will do whatever it wants with the texture memory.
  This is a good option if you know that every single pixel will be touched
  in the render pass.

The store_op field determines what is done with the color results of the
render pass.

- STORE: Stores the results of the render pass in the texture. Not
  recommended for multisample textures as it requires significant memory
  bandwidth.
- DONT_CARE: The driver will do whatever it wants with the texture memory.
  This is often a good option for depth/stencil textures.
- RESOLVE: Resolves a multisample texture into resolve_texture, which must
  have a sample count of 1. Then the driver may discard the multisample
  texture memory. This is the most performant method of resolving a
  multisample target.
- RESOLVE_AND_STORE: Resolves a multisample texture into the
  resolve_texture, which must have a sample count of 1. Then the driver
  stores the multisample texture's contents. Not recommended as it requires
  significant memory bandwidth.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

