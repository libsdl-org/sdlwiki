###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUSwapchainComposition

Specifies the texture format and colorspace of the swapchain textures.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUSwapchainComposition
{
    SDL_GPU_SWAPCHAINCOMPOSITION_SDR,
    SDL_GPU_SWAPCHAINCOMPOSITION_SDR_LINEAR,
    SDL_GPU_SWAPCHAINCOMPOSITION_HDR_EXTENDED_LINEAR,
    SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2048
} SDL_GPUSwapchainComposition;
```

## Remarks

SDR will always be supported. Other compositions may not be supported on
certain systems.

It is recommended to query
[SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)
after claiming the window if you wish to change the swapchain composition
from SDR.

SDR: B8G8R8A8 or R8G8B8A8 swapchain. Pixel values are in nonlinear sRGB
encoding. SDR_LINEAR: B8G8R8A8_SRGB or R8G8B8A8_SRGB swapchain. Pixel
values are in nonlinear sRGB encoding. HDR_EXTENDED_LINEAR:
R16G16B16A16_SFLOAT swapchain. Pixel values are in extended linear
encoding. HDR10_ST2048: A2R10G10B10 or A2B10G10R10 swapchain. Pixel values
are in PQ ST2048 encoding.

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_SetGPUSwapchainParameters](SDL_SetGPUSwapchainParameters)
- [SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

