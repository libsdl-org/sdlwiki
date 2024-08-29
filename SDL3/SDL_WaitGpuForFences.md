###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitGpuForFences

Blocks the thread until the given fences are signaled.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_WaitGpuForFences(
    SDL_GpuDevice *device,
    SDL_bool waitAll,
    SDL_GpuFence **pFences,
    Uint32 fenceCount);
```

## Function Parameters

|                                  |                |                                                                                    |
| -------------------------------- | -------------- | ---------------------------------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device**     | a GPU context.                                                                     |
| [SDL_bool](SDL_bool)             | **waitAll**    | if 0, wait for any fence to be signaled, if 1, wait for all fences to be signaled. |
| [SDL_GpuFence](SDL_GpuFence) **  | **pFences**    | an array of fences to wait on.                                                     |
| Uint32                           | **fenceCount** | the number of fences in the pFences array.                                         |

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence)
- [SDL_WaitGpu](SDL_WaitGpu)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

