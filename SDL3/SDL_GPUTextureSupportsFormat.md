###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUTextureSupportsFormat

Determines whether a texture format is supported for a given type and usage.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_GPUTextureSupportsFormat(
    SDL_GPUDevice *device,
    SDL_GPUTextureFormat format,
    SDL_GPUTextureType type,
    SDL_GPUTextureUsageFlags usage);
```

## Function Parameters

|                                                      |            |                                            |
| ---------------------------------------------------- | ---------- | ------------------------------------------ |
| [SDL_GPUDevice](SDL_GPUDevice) *                     | **device** | a GPU context.                             |
| [SDL_GPUTextureFormat](SDL_GPUTextureFormat)         | **format** | the texture format to check.               |
| [SDL_GPUTextureType](SDL_GPUTextureType)             | **type**   | the type of texture (2D, 3D, Cube).        |
| [SDL_GPUTextureUsageFlags](SDL_GPUTextureUsageFlags) | **usage**  | a bitmask of all usage scenarios to check. |

## Return Value

(bool) Returns whether the texture format is supported for this type and
usage.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

