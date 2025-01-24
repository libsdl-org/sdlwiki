# SDL_GPUSamplerCreateInfo

A structure specifying the parameters of a sampler.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUSamplerCreateInfo
{
    SDL_GPUFilter min_filter;                  /**< The minification filter to apply to lookups. */
    SDL_GPUFilter mag_filter;                  /**< The magnification filter to apply to lookups. */
    SDL_GPUSamplerMipmapMode mipmap_mode;      /**< The mipmap filter to apply to lookups. */
    SDL_GPUSamplerAddressMode address_mode_u;  /**< The addressing mode for U coordinates outside [0, 1). */
    SDL_GPUSamplerAddressMode address_mode_v;  /**< The addressing mode for V coordinates outside [0, 1). */
    SDL_GPUSamplerAddressMode address_mode_w;  /**< The addressing mode for W coordinates outside [0, 1). */
    float mip_lod_bias;                        /**< The bias to be added to mipmap LOD calculation. */
    float max_anisotropy;                      /**< The anisotropy value clamp used by the sampler. If enable_anisotropy is false, this is ignored. */
    SDL_GPUCompareOp compare_op;               /**< The comparison operator to apply to fetched data before filtering. */
    float min_lod;                             /**< Clamps the minimum of the computed LOD value. */
    float max_lod;                             /**< Clamps the maximum of the computed LOD value. */
    bool enable_anisotropy;                /**< true to enable anisotropic filtering. */
    bool enable_compare;                   /**< true to enable comparison against a reference value during lookups. */
    Uint8 padding1;
    Uint8 padding2;

    SDL_PropertiesID props;                    /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUSamplerCreateInfo;
```

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUSampler](SDL_CreateGPUSampler)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

