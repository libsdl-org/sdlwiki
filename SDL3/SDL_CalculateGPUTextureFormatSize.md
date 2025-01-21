###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CalculateGPUTextureFormatSize

Calculate the size in bytes of a texture format with dimensions.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
Uint32 SDL_CalculateGPUTextureFormatSize(
    SDL_GPUTextureFormat format,
    Uint32 width,
    Uint32 height,
    Uint32 depth_or_layer_count);
```

## Function Parameters

|                                              |                          |                                                 |
| -------------------------------------------- | ------------------------ | ----------------------------------------------- |
| [SDL_GPUTextureFormat](SDL_GPUTextureFormat) | **format**               | a texture format.                               |
| [Uint32](Uint32)                             | **width**                | width in pixels.                                |
| [Uint32](Uint32)                             | **height**               | height in pixels.                               |
| [Uint32](Uint32)                             | **depth_or_layer_count** | depth for 3D textures or layer count otherwise. |

## Return Value

([Uint32](Uint32)) Returns the size of a texture with this format and
dimensions.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

