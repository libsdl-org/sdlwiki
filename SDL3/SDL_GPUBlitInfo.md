###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUBlitInfo

A structure containing parameters for a blit command.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUBlitInfo {
    SDL_GPUBlitRegion source;       /**< The source region for the blit. */
    SDL_GPUBlitRegion destination;  /**< The destination region for the blit. */
    SDL_GPULoadOp load_op;          /**< What is done with the contents of the destination before the blit. */
    SDL_FColor clear_color;         /**< The color to clear the destination region to before the blit. Ignored if load_op is not SDL_GPU_LOADOP_CLEAR. */
    SDL_FlipMode flip_mode;         /**< The flip mode for the source region. */
    SDL_GPUFilter filter;           /**< The filter mode used when blitting. */
    SDL_bool cycle;                 /**< SDL_TRUE cycles the destination texture if it is already bound. */
    Uint8 padding;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUBlitInfo;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_BlitGPUTexture](SDL_BlitGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

