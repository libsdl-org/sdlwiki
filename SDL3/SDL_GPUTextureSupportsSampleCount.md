###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUTextureSupportsSampleCount

Determines if a sample count for a texture format is supported.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_GPUTextureSupportsSampleCount(
    SDL_GPUDevice *device,
    SDL_GPUTextureFormat format,
    SDL_GPUSampleCount sample_count);
```

## Function Parameters

|                                              |                  |                              |
| -------------------------------------------- | ---------------- | ---------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *             | **device**       | a GPU context.               |
| [SDL_GPUTextureFormat](SDL_GPUTextureFormat) | **format**       | the texture format to check. |
| [SDL_GPUSampleCount](SDL_GPUSampleCount)     | **sample_count** | the sample count to check.   |

## Return Value

(bool) Returns a hardware-specific version of min(preferred, possible).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

