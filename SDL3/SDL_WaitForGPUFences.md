###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WaitForGPUFences

Blocks the thread until the given fences are signaled.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_WaitForGPUFences(
    SDL_GPUDevice *device,
    bool wait_all,
    SDL_GPUFence *const *fences,
    Uint32 num_fences);
```

## Function Parameters

|                                       |                |                                                                                    |
| ------------------------------------- | -------------- | ---------------------------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *      | **device**     | a GPU context.                                                                     |
| bool                                  | **wait_all**   | if 0, wait for any fence to be signaled, if 1, wait for all fences to be signaled. |
| [SDL_GPUFence](SDL_GPUFence) *const * | **fences**     | an array of fences to wait on.                                                     |
| [Uint32](Uint32)                      | **num_fences** | the number of fences in the fences array.                                          |

## Return Value

(bool) Returns true on success, false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)
- [SDL_WaitForGPUIdle](SDL_WaitForGPUIdle)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

