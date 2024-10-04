###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUFilter

Specifies a filter operation used by a sampler.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUFilter
{
    SDL_GPU_FILTER_NEAREST,  /**< Point filtering. */
    SDL_GPU_FILTER_LINEAR    /**< Linear filtering. */
} SDL_GPUFilter;
```

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUSampler](SDL_CreateGPUSampler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

