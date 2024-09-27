###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUComputePipeline

Creates a pipeline object to be used in a compute workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUComputePipeline* SDL_CreateGPUComputePipeline(
    SDL_GPUDevice *device,
    const SDL_GPUComputePipelineCreateInfo *createinfo);
```

## Function Parameters

|                                                                              |                |                                                                  |
| ---------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                                             | **device**     | a GPU Context.                                                   |
| const [SDL_GPUComputePipelineCreateInfo](SDL_GPUComputePipelineCreateInfo) * | **createinfo** | a struct describing the state of the compute pipeline to create. |

## Return Value

([SDL_GPUComputePipeline](SDL_GPUComputePipeline) *) Returns a compute
pipeline object on success, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Shader resource bindings must be authored to follow a particular order
depending on the shader format.

For SPIR-V shaders, use the following resource sets:

- 0: Sampled textures, followed by read-only storage textures, followed by
  read-only storage buffers
- 1: Write-only storage textures, followed by write-only storage buffers
- 2: Uniform buffers

For DXBC Shader Model 5_0 shaders, use the following register order:

- t registers: Sampled textures, followed by read-only storage textures,
  followed by read-only storage buffers
- u registers: Write-only storage textures, followed by write-only storage
  buffers
- b registers: Uniform buffers

For DXIL shaders, use the following register order:

- (t[n], space0): Sampled textures, followed by read-only storage textures,
  followed by read-only storage buffers
- (u[n], space1): Write-only storage textures, followed by write-only
  storage buffers
- (b[n], space2): Uniform buffers

For MSL/metallib, use the following order:

- [[buffer]]: Uniform buffers, followed by write-only storage buffers,
  followed by write-only storage buffers
- [[texture]]: Sampled textures, followed by read-only storage textures,
  followed by write-only storage textures

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BindGPUComputePipeline](SDL_BindGPUComputePipeline)
- [SDL_ReleaseGPUComputePipeline](SDL_ReleaseGPUComputePipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

