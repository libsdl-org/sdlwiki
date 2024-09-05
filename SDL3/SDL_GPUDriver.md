###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUDriver

Specifies a backend API supported by [SDL_GPU](SDL_GPU).

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUDriver
{
    SDL_GPU_DRIVER_INVALID = -1,
    SDL_GPU_DRIVER_PRIVATE, /* NDA'd platforms */
    SDL_GPU_DRIVER_VULKAN,
    SDL_GPU_DRIVER_D3D11,
    SDL_GPU_DRIVER_D3D12,
    SDL_GPU_DRIVER_METAL
} SDL_GPUDriver;
```

## Remarks

Only one of these will be in use at a time.

## Version

This enum is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

