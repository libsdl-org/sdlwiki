###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseGpuBuffer

Frees the given buffer as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGpuBuffer(
    SDL_GpuDevice *device,
    SDL_GpuBuffer *buffer);
```

## Function Parameters

|                                  |            |                           |
| -------------------------------- | ---------- | ------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context.            |
| [SDL_GpuBuffer](SDL_GpuBuffer) * | **buffer** | a buffer to be destroyed. |

## Remarks

You must not reference the buffer after calling this function.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

