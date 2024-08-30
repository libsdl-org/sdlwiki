###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseGPUFence

Releases a fence obtained from [SDL_SubmitGPUAndAcquireFence](SDL_SubmitGPUAndAcquireFence).

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGPUFence(
    SDL_GPUDevice *device,
    SDL_GPUFence *fence);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context. |
| [SDL_GPUFence](SDL_GPUFence) *   | **fence**  | a fence.       |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SubmitGPUAndAcquireFence](SDL_SubmitGPUAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

