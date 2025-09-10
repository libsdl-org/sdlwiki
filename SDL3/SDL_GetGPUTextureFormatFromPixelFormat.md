# SDL_GetGPUTextureFormatFromPixelFormat

Get the GPU texture format corresponding to an SDL pixel format.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTextureFormat SDL_GetGPUTextureFormatFromPixelFormat(SDL_PixelFormat format);
```

## Function Parameters

|                                    |            |                 |
| ---------------------------------- | ---------- | --------------- |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | a pixel format. |

## Return Value

([SDL_GPUTextureFormat](SDL_GPUTextureFormat)) Returns the corresponding
GPU texture format, or
[SDL_GPU_TEXTUREFORMAT_INVALID](SDL_GPU_TEXTUREFORMAT_INVALID) if there is
no corresponding GPU texture format.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

