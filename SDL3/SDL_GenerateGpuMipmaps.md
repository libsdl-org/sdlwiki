###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GenerateGpuMipmaps

Generates mipmaps for the given texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_GenerateGpuMipmaps(
    SDL_GpuCommandBuffer *commandBuffer,
    SDL_GpuTexture *texture);
```

## Function Parameters

|                                                |                   |                                       |
| ---------------------------------------------- | ----------------- | ------------------------------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a commandBuffer.                      |
| [SDL_GpuTexture](SDL_GpuTexture) *             | **texture**       | a texture with more than 1 mip level. |

## Remarks

This function must not be called inside of any pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


