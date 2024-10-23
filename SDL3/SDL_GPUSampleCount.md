###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUSampleCount

Specifies the sample count of a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUSampleCount
{
    SDL_GPU_SAMPLECOUNT_1,  /**< No multisampling. */
    SDL_GPU_SAMPLECOUNT_2,  /**< MSAA 2x */
    SDL_GPU_SAMPLECOUNT_4,  /**< MSAA 4x */
    SDL_GPU_SAMPLECOUNT_8   /**< MSAA 8x */
} SDL_GPUSampleCount;
```

## Remarks

Used in multisampling. Note that this value only applies when the texture
is used as a render target.

## Version

This enum is available since SDL 3.1.3

## See Also

- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)
- [SDL_GPUTextureSupportsSampleCount](SDL_GPUTextureSupportsSampleCount)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

