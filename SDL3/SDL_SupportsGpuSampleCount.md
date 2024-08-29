###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SupportsGpuSampleCount

Determines if a sample count for a texture format is supported.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_SupportsGpuSampleCount(
    SDL_GpuDevice *device,
    SDL_GpuTextureFormat format,
    SDL_GpuSampleCount sampleCount);
```

## Function Parameters

|                                              |                 |                              |
| -------------------------------------------- | --------------- | ---------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *             | **device**      | a GPU context.               |
| [SDL_GpuTextureFormat](SDL_GpuTextureFormat) | **format**      | the texture format to check. |
| [SDL_GpuSampleCount](SDL_GpuSampleCount)     | **sampleCount** | the sample count to check.   |

## Return Value

([SDL_bool](SDL_bool)) Returns a hardware-specific version of
min(preferred, possible).

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

