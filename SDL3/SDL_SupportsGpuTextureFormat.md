###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SupportsGpuTextureFormat

Determines whether a texture format is supported for a given type and usage.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_SupportsGpuTextureFormat(
    SDL_GpuDevice *device,
    SDL_GpuTextureFormat format,
    SDL_GpuTextureType type,
    SDL_GpuTextureUsageFlags usage);
```

## Function Parameters

|                                                      |            |                                            |
| ---------------------------------------------------- | ---------- | ------------------------------------------ |
| [SDL_GpuDevice](SDL_GpuDevice) *                     | **device** | a GPU context.                             |
| [SDL_GpuTextureFormat](SDL_GpuTextureFormat)         | **format** | the texture format to check.               |
| [SDL_GpuTextureType](SDL_GpuTextureType)             | **type**   | the type of texture (2D, 3D, Cube).        |
| [SDL_GpuTextureUsageFlags](SDL_GpuTextureUsageFlags) | **usage**  | a bitmask of all usage scenarios to check. |

## Return Value

([SDL_bool](SDL_bool)) Returns whether the texture format is supported for
this type and usage.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

