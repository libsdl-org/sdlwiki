###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BindGPUFragmentSamplers

Binds texture-sampler pairs for use on the fragment shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUFragmentSamplers(
    SDL_GPURenderPass *render_pass,
    Uint32 first_slot,
    const SDL_GPUTextureSamplerBinding *texture_sampler_bindings,
    Uint32 num_bindings);
```

## Function Parameters

|                                                                      |                              |                                                             |
| -------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) *                             | **render_pass**              | a render pass handle.                                       |
| [Uint32](Uint32)                                                     | **first_slot**               | the fragment sampler slot to begin binding from.            |
| const [SDL_GPUTextureSamplerBinding](SDL_GPUTextureSamplerBinding) * | **texture_sampler_bindings** | an array of texture-sampler binding structs.                |
| [Uint32](Uint32)                                                     | **num_bindings**             | the number of texture-sampler pairs to bind from the array. |

## Remarks

The textures must have been created with
[SDL_GPU_TEXTUREUSAGE_SAMPLER](SDL_GPU_TEXTUREUSAGE_SAMPLER).

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

