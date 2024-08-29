###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuShader

Creates a shader to be used when creating a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuShader* SDL_CreateGpuShader(
    SDL_GpuDevice *device,
    SDL_GpuShaderCreateInfo *shaderCreateInfo);
```

## Function Parameters

|                                                      |                      |                                                      |
| ---------------------------------------------------- | -------------------- | ---------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                     | **device**           | a GPU Context.                                       |
| [SDL_GpuShaderCreateInfo](SDL_GpuShaderCreateInfo) * | **shaderCreateInfo** | a struct describing the state of the desired shader. |

## Return Value

([SDL_GpuShader](SDL_GpuShader) *) Returns a shader object on success, or
NULL on failure.

## Remarks

Shader resource bindings must be authored to follow a particular order
depending on the shader format.

For SPIR-V shaders, use the following resource sets: For vertex shaders: 0:
Sampled textures, followed by storage textures, followed by storage buffers
1: Uniform buffers For fragment shaders: 2: Sampled textures, followed by
storage textures, followed by storage buffers 3: Uniform buffers

For DXBC Shader Model 5_0 shaders, use the following register order: For t
registers: Sampled textures, followed by storage textures, followed by
storage buffers For s registers: Samplers with indices corresponding to the
sampled textures For b registers: Uniform buffers

For DXIL shaders, use the following register order: For vertex shaders:
(t[n], space0): Sampled textures, followed by storage textures, followed by
storage buffers (s[n], space0): Samplers with indices corresponding to the
sampled textures (b[n], space1): Uniform buffers For pixel shaders: (t[n],
space2): Sampled textures, followed by storage textures, followed by
storage buffers (s[n], space2): Samplers with indices corresponding to the
sampled textures (b[n], space3): Uniform buffers

For MSL/metallib, use the following order: For [[texture]]: Sampled
textures, followed by storage textures For [[sampler]]: Samplers with
indices corresponding to the sampled textures For [[buffer]]: Uniform
buffers, followed by storage buffers. Vertex buffer 0 is bound at
[[buffer(30)]], vertex buffer 1 at [[buffer(29)]], and so on. Rather than
manually authoring vertex buffer indices, use the [[stage_in]] attribute
which will automatically use the vertex input information from the
[SDL_GpuPipeline](SDL_GpuPipeline).

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_CreateGpuGraphicsPipeline](SDL_CreateGpuGraphicsPipeline)
- [SDL_ReleaseGpuShader](SDL_ReleaseGpuShader)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

