###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUTextureUsageFlags

Specifies how a texture is intended to be used by the client.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef Uint32 SDL_GPUTextureUsageFlags;

#define SDL_GPU_TEXTUREUSAGE_SAMPLER               (1u << 0) /**< Texture supports sampling. */
#define SDL_GPU_TEXTUREUSAGE_COLOR_TARGET          (1u << 1) /**< Texture is a color render target. */
#define SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET  (1u << 2) /**< Texture is a depth stencil target. */
#define SDL_GPU_TEXTUREUSAGE_GRAPHICS_STORAGE_READ (1u << 3) /**< Texture supports storage reads in graphics stages. */
#define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ  (1u << 4) /**< Texture supports storage reads in the compute stage. */
#define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE (1u << 5) /**< Texture supports storage writes in the compute stage. */
```

## Remarks

A texture must have at least one usage flag. Note that some usage flag
combinations are invalid.

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

