###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGpuDriver

Returns the backend used to create this GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuDriver SDL_GetGpuDriver(SDL_GpuDevice *device);
```

## Function Parameters

|                                  |            |                         |
| -------------------------------- | ---------- | ----------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context to query. |

## Return Value

([SDL_GpuDriver](SDL_GpuDriver)) Returns an [SDL_GpuDriver](SDL_GpuDriver)
value, or [SDL_GPU_DRIVER_INVALID](SDL_GPU_DRIVER_INVALID) on error.

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

