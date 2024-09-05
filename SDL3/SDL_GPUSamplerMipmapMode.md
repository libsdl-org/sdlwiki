###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUSamplerMipmapMode

Specifies a mipmap mode used by a sampler.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUSamplerMipmapMode
{
    SDL_GPU_SAMPLERMIPMAPMODE_NEAREST,  /**< Point filtering. */
    SDL_GPU_SAMPLERMIPMAPMODE_LINEAR    /**< Linear filtering. */
} SDL_GPUSamplerMipmapMode;
```

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUSampler](SDL_CreateGPUSampler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

