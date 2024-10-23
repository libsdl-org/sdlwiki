###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUTextureCreateInfo

A structure specifying the parameters of a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUTextureCreateInfo
{
    SDL_GPUTextureType type;          /**< The base dimensionality of the texture. */
    SDL_GPUTextureFormat format;      /**< The pixel format of the texture. */
    SDL_GPUTextureUsageFlags usage;   /**< How the texture is intended to be used by the client. */
    Uint32 width;                     /**< The width of the texture. */
    Uint32 height;                    /**< The height of the texture. */
    Uint32 layer_count_or_depth;      /**< The layer count or depth of the texture. This value is treated as a layer count on 2D array textures, and as a depth value on 3D textures. */
    Uint32 num_levels;                /**< The number of mip levels in the texture. */
    SDL_GPUSampleCount sample_count;  /**< The number of samples per texel. Only applies if the texture is used as a render target. */

    SDL_PropertiesID props;           /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUTextureCreateInfo;
```

## Remarks

Usage flags can be bitwise OR'd together for combinations of usages. Note
that certain usage combinations are invalid, for example SAMPLER and
GRAPHICS_STORAGE.

## Version

This struct is available since SDL 3.1.3

## See Also

- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

