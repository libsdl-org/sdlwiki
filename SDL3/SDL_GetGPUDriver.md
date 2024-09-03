###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGPUDriver

Returns the backend used to create this GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUDriver SDL_GetGPUDriver(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                         |
| -------------------------------- | ---------- | ----------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context to query. |

## Return Value

([SDL_GPUDriver](SDL_GPUDriver)) Returns an [SDL_GPUDriver](SDL_GPUDriver)
value, or [SDL_GPU_DRIVER_INVALID](SDL_GPU_DRIVER_INVALID) on error.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)
