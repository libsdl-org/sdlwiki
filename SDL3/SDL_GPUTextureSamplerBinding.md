###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUTextureSamplerBinding

A structure specifying parameters in a sampler binding call.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUTextureSamplerBinding
{
    SDL_GPUTexture *texture;  /**< The texture to bind. Must have been created with SDL_GPU_TEXTUREUSAGE_SAMPLER. */
    SDL_GPUSampler *sampler;  /**< The sampler to bind. */
} SDL_GPUTextureSamplerBinding;
```

## Version

This struct is available since SDL 3.1.3

## See Also

- [SDL_BindGPUVertexSamplers](SDL_BindGPUVertexSamplers)
- [SDL_BindGPUFragmentSamplers](SDL_BindGPUFragmentSamplers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

