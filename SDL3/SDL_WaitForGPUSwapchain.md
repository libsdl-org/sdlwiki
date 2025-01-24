# SDL_WaitForGPUSwapchain

Blocks the thread until a swapchain texture is available to be acquired.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_WaitForGPUSwapchain(
    SDL_GPUDevice *device,
    SDL_Window *window);
```

## Function Parameters

|                                  |            |                                 |
| -------------------------------- | ---------- | ------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context.                  |
| [SDL_Window](SDL_Window) *       | **window** | a window that has been claimed. |

## Return Value

(bool) Returns true on success, false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called from the thread that created the
window.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)
- [SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)
- [SDL_SetGPUAllowedFramesInFlight](SDL_SetGPUAllowedFramesInFlight)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

