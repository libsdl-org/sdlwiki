###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitGpu

Blocks the thread until the GPU is completely idle.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_WaitGpu(
    SDL_GpuDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context. |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_WaitGpuForFences](SDL_WaitGpuForFences)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


