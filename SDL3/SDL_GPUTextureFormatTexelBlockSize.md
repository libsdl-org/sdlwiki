###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUTextureFormatTexelBlockSize

Obtains the texel block size for a texture format.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
Uint32 SDL_GPUTextureFormatTexelBlockSize(
    SDL_GPUTextureFormat format);
```

## Function Parameters

|                                              |            |                                                        |
| -------------------------------------------- | ---------- | ------------------------------------------------------ |
| [SDL_GPUTextureFormat](SDL_GPUTextureFormat) | **format** | the texture format you want to know the texel size of. |

## Return Value

(Uint32) Returns the texel block size of the texture format.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

