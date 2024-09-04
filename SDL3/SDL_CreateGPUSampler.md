###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUSampler

Creates a sampler object to be used when binding textures in a graphics workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUSampler* SDL_CreateGPUSampler(
    SDL_GPUDevice *device,
    const SDL_GPUSamplerCreateInfo *samplerCreateInfo);
```

## Function Parameters

|                                                              |                       |                                                       |
| ------------------------------------------------------------ | --------------------- | ----------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                             | **device**            | a GPU Context.                                        |
| const [SDL_GPUSamplerCreateInfo](SDL_GPUSamplerCreateInfo) * | **samplerCreateInfo** | a struct describing the state of the desired sampler. |

## Return Value

([SDL_GPUSampler](SDL_GPUSampler) *) Returns a sampler object on success,
or NULL on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BindGPUVertexSamplers](SDL_BindGPUVertexSamplers)
- [SDL_BindGPUFragmentSamplers](SDL_BindGPUFragmentSamplers)
- [SDL_ReleaseSampler](SDL_ReleaseSampler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

