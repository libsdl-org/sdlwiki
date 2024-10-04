###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUColorComponentFlags

Specifies which color components are written in a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef Uint8 SDL_GPUColorComponentFlags;

#define SDL_GPU_COLORCOMPONENT_R (1u << 0) /**< the red component */
#define SDL_GPU_COLORCOMPONENT_G (1u << 1) /**< the green component */
#define SDL_GPU_COLORCOMPONENT_B (1u << 2) /**< the blue component */
#define SDL_GPU_COLORCOMPONENT_A (1u << 3) /**< the alpha component */
```

## Version

This datatype is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

