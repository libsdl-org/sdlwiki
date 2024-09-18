###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_QueryGPUFence

Checks the status of a fence.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_QueryGPUFence(
    SDL_GPUDevice *device,
    SDL_GPUFence *fence);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context. |
| [SDL_GPUFence](SDL_GPUFence) *   | **fence**  | a fence.       |

## Return Value

(bool) Returns true if the fence is signaled, false if it is not.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

