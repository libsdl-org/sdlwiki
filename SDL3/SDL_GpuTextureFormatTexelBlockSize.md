###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GpuTextureFormatTexelBlockSize

Obtains the texel block size for a texture format.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
Uint32 SDL_GpuTextureFormatTexelBlockSize(
    SDL_GpuTextureFormat textureFormat);
```

## Function Parameters

|                                              |                   |                                                        |
| -------------------------------------------- | ----------------- | ------------------------------------------------------ |
| [SDL_GpuTextureFormat](SDL_GpuTextureFormat) | **textureFormat** | the texture format you want to know the texel size of. |

## Return Value

(Uint32) Returns the texel block size of the texture format.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UploadToGpuTexture](SDL_UploadToGpuTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


