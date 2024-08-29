###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseGpuFence

Releases a fence obtained from [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence).

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGpuFence(
    SDL_GpuDevice *device,
    SDL_GpuFence *fence);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context. |
| [SDL_GpuFence](SDL_GpuFence) *   | **fence**  | a fence.       |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

