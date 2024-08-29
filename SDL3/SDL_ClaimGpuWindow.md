###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClaimGpuWindow

Claims a window, creating a swapchain structure for it.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_ClaimGpuWindow(
    SDL_GpuDevice *device,
    SDL_Window *window);
```

## Function Parameters

|                                  |            |                              |
| -------------------------------- | ---------- | ---------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context.               |
| [SDL_Window](SDL_Window) *       | **window** | an [SDL_Window](SDL_Window). |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success, otherwise
[SDL_FALSE](SDL_FALSE).

## Remarks

This must be called before
[SDL_AcquireGpuSwapchainTexture](SDL_AcquireGpuSwapchainTexture) is called
using the window.

The swapchain will be created with
[SDL_GPU_SWAPCHAINCOMPOSITION_SDR](SDL_GPU_SWAPCHAINCOMPOSITION_SDR) and
[SDL_GPU_PRESENTMODE_VSYNC](SDL_GPU_PRESENTMODE_VSYNC). If you want to have
different swapchain parameters, you must call SetSwapchainParameters after
claiming the window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AcquireGpuSwapchainTexture](SDL_AcquireGpuSwapchainTexture)
- [SDL_UnclaimGpuWindow](SDL_UnclaimGpuWindow)
- [SDL_SupportsGpuPresentMode](SDL_SupportsGpuPresentMode)
- [SDL_SupportsGpuSwapchainComposition](SDL_SupportsGpuSwapchainComposition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

