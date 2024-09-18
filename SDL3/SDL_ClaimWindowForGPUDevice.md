###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClaimWindowForGPUDevice

Claims a window, creating a swapchain structure for it.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_ClaimWindowForGPUDevice(
    SDL_GPUDevice *device,
    SDL_Window *window);
```

## Function Parameters

|                                  |            |                              |
| -------------------------------- | ---------- | ---------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context.               |
| [SDL_Window](SDL_Window) *       | **window** | an [SDL_Window](SDL_Window). |

## Return Value

(bool) Returns true on success, otherwise false.

## Remarks

This must be called before
[SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture) is called
using the window.

The swapchain will be created with
[SDL_GPU_SWAPCHAINCOMPOSITION_SDR](SDL_GPU_SWAPCHAINCOMPOSITION_SDR) and
[SDL_GPU_PRESENTMODE_VSYNC](SDL_GPU_PRESENTMODE_VSYNC). If you want to have
different swapchain parameters, you must call
[SDL_SetGPUSwapchainParameters](SDL_SetGPUSwapchainParameters) after
claiming the window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)
- [SDL_ReleaseWindowFromGPUDevice](SDL_ReleaseWindowFromGPUDevice)
- [SDL_WindowSupportsGPUPresentMode](SDL_WindowSupportsGPUPresentMode)
- [SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

