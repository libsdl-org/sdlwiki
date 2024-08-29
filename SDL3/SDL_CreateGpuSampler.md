###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuSampler

Creates a sampler object to be used when binding textures in a graphics workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuSampler* SDL_CreateGpuSampler(
    SDL_GpuDevice *device,
    SDL_GpuSamplerCreateInfo *samplerCreateInfo);
```

## Function Parameters

|                                                        |                       |                                                       |
| ------------------------------------------------------ | --------------------- | ----------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                       | **device**            | a GPU Context.                                        |
| [SDL_GpuSamplerCreateInfo](SDL_GpuSamplerCreateInfo) * | **samplerCreateInfo** | a struct describing the state of the desired sampler. |

## Return Value

([SDL_GpuSampler](SDL_GpuSampler) *) Returns a sampler object on success,
or NULL on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BindGpuVertexSamplers](SDL_BindGpuVertexSamplers)
- [SDL_BindGpuFragmentSamplers](SDL_BindGpuFragmentSamplers)
- [SDL_ReleaseSampler](SDL_ReleaseSampler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


