###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGpuVertexSamplers

Binds texture-sampler pairs for use on the vertex shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGpuVertexSamplers(
    SDL_GpuRenderPass *renderPass,
    Uint32 firstSlot,
    SDL_GpuTextureSamplerBinding *textureSamplerBindings,
    Uint32 bindingCount);
```

## Function Parameters

|                                                                |                            |                                                             |
| -------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------- |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) *                       | **renderPass**             | a render pass handle.                                       |
| Uint32                                                         | **firstSlot**              | the vertex sampler slot to begin binding from.              |
| [SDL_GpuTextureSamplerBinding](SDL_GpuTextureSamplerBinding) * | **textureSamplerBindings** | an array of texture-sampler binding structs.                |
| Uint32                                                         | **bindingCount**           | the number of texture-sampler pairs to bind from the array. |

## Remarks

The textures must have been created with
[SDL_GPU_TEXTUREUSAGE_SAMPLER_BIT](SDL_GPU_TEXTUREUSAGE_SAMPLER_BIT).

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

