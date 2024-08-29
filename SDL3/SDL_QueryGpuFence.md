###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_QueryGpuFence

Checks the status of a fence.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_QueryGpuFence(
    SDL_GpuDevice *device,
    SDL_GpuFence *fence);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context. |
| [SDL_GpuFence](SDL_GpuFence) *   | **fence**  | a fence.       |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the fence is
signaled, [SDL_FALSE](SDL_FALSE) if it is not.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

