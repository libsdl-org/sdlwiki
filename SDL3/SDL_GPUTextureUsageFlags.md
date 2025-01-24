# SDL_GPUTextureUsageFlags

Specifies how a texture is intended to be used by the client.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef Uint32 SDL_GPUTextureUsageFlags;

#define SDL_GPU_TEXTUREUSAGE_SAMPLER                                 (1u << 0) /**< Texture supports sampling. */
#define SDL_GPU_TEXTUREUSAGE_COLOR_TARGET                            (1u << 1) /**< Texture is a color render target. */
#define SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET                    (1u << 2) /**< Texture is a depth stencil target. */
#define SDL_GPU_TEXTUREUSAGE_GRAPHICS_STORAGE_READ                   (1u << 3) /**< Texture supports storage reads in graphics stages. */
#define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ                    (1u << 4) /**< Texture supports storage reads in the compute stage. */
#define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE                   (1u << 5) /**< Texture supports storage writes in the compute stage. */
#define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE (1u << 6) /**< Texture supports reads and writes in the same compute shader. This is NOT equivalent to READ | WRITE. */
```

## Remarks

A texture must have at least one usage flag. Note that some usage flag
combinations are invalid.

With regards to compute storage usage, READ | WRITE means that you can have
shader A that only writes into the texture and shader B that only reads
from the texture and bind the same texture to either shader respectively.
SIMULTANEOUS means that you can do reads and writes within the same shader
or compute pass. It also implies that atomic ops can be used, since those
are read-modify-write operations. If you use SIMULTANEOUS, you are
responsible for avoiding data races, as there is no data synchronization
within a compute pass. Note that SIMULTANEOUS usage is only supported by a
limited number of texture formats.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

