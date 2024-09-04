###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGPUFragmentSamplers

Binds texture-sampler pairs for use on the fragment shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUFragmentSamplers(
    SDL_GPURenderPass *renderPass,
    Uint32 firstSlot,
    const SDL_GPUTextureSamplerBinding *textureSamplerBindings,
    Uint32 bindingCount);
```

## Function Parameters

|                                                                      |                            |                                                             |
| -------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) *                             | **renderPass**             | a render pass handle.                                       |
| Uint32                                                               | **firstSlot**              | the fragment sampler slot to begin binding from.            |
| const [SDL_GPUTextureSamplerBinding](SDL_GPUTextureSamplerBinding) * | **textureSamplerBindings** | an array of texture-sampler binding structs.                |
| Uint32                                                               | **bindingCount**           | the number of texture-sampler pairs to bind from the array. |

## Remarks

The textures must have been created with
[SDL_GPU_TEXTUREUSAGE_SAMPLER](SDL_GPU_TEXTUREUSAGE_SAMPLER).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

