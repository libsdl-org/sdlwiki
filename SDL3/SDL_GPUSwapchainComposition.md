###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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
    SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2084
} SDL_GPUSwapchainComposition;
```

## Remarks

SDR will always be supported. Other compositions may not be supported on
certain systems.

It is recommended to query
[SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)
after claiming the window if you wish to change the swapchain composition
from SDR.

- SDR: B8G8R8A8 or R8G8B8A8 swapchain. Pixel values are in sRGB encoding.
- SDR_LINEAR: B8G8R8A8_SRGB or R8G8B8A8_SRGB swapchain. Pixel values are
  stored in memory in sRGB encoding but accessed in shaders in "linear
  sRGB" encoding which is sRGB but with a linear transfer function.
- HDR_EXTENDED_LINEAR: R16G16B16A16_FLOAT swapchain. Pixel values are in
  extended linear sRGB encoding and permits values outside of the [0, 1]
  range.
- HDR10_ST2084: A2R10G10B10 or A2B10G10R10 swapchain. Pixel values are in
  BT.2020 ST2084 (PQ) encoding.

## Version

This enum is available since SDL 3.1.3

## See Also

- [SDL_SetGPUSwapchainParameters](SDL_SetGPUSwapchainParameters)
- [SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)
- [SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

