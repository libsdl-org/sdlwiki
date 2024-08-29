###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SupportsGpuSwapchainComposition

Determines whether a swapchain composition is supported by the window.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_SupportsGpuSwapchainComposition(
    SDL_GpuDevice *device,
    SDL_Window *window,
    SDL_GpuSwapchainComposition swapchainComposition);
```

## Function Parameters

|                                                            |                          |                                     |
| ---------------------------------------------------------- | ------------------------ | ----------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                           | **device**               | a GPU context.                      |
| [SDL_Window](SDL_Window) *                                 | **window**               | an [SDL_Window](SDL_Window).        |
| [SDL_GpuSwapchainComposition](SDL_GpuSwapchainComposition) | **swapchainComposition** | the swapchain composition to check. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if supported,
[SDL_FALSE](SDL_FALSE) if unsupported (or on error).

## Remarks

The window must be claimed before calling this function.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ClaimGpuWindow](SDL_ClaimGpuWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


