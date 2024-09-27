###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUShader

Creates a shader to be used when creating a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUShader* SDL_CreateGPUShader(
    SDL_GPUDevice *device,
    const SDL_GPUShaderCreateInfo *createinfo);
```

## Function Parameters

|                                                            |                |                                                        |
| ---------------------------------------------------------- | -------------- | ------------------------------------------------------ |
| [SDL_GPUDevice](SDL_GPUDevice) *                           | **device**     | a GPU Context.                                         |
| const [SDL_GPUShaderCreateInfo](SDL_GPUShaderCreateInfo) * | **createinfo** | a struct describing the state of the shader to create. |

## Return Value

([SDL_GPUShader](SDL_GPUShader) *) Returns a shader object on success, or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Shader resource bindings must be authored to follow a particular order
depending on the shader format.

For SPIR-V shaders, use the following resource sets:

For vertex shaders:

- 0: Sampled textures, followed by storage textures, followed by storage
  buffers
- 1: Uniform buffers

For fragment shaders:

- 2: Sampled textures, followed by storage textures, followed by storage
  buffers
- 3: Uniform buffers

For DXBC Shader Model 5_0 shaders, use the following register order:

- t registers: Sampled textures, followed by storage textures, followed by
  storage buffers
- s registers: Samplers with indices corresponding to the sampled textures
- b registers: Uniform buffers

For DXIL shaders, use the following register order:

For vertex shaders:

- (t[n], space0): Sampled textures, followed by storage textures, followed
  by storage buffers
- (s[n], space0): Samplers with indices corresponding to the sampled
  textures
- (b[n], space1): Uniform buffers

For pixel shaders:

- (t[n], space2): Sampled textures, followed by storage textures, followed
  by storage buffers
- (s[n], space2): Samplers with indices corresponding to the sampled
  textures
- (b[n], space3): Uniform buffers

For MSL/metallib, use the following order:

- [[texture]]: Sampled textures, followed by storage textures
- [[sampler]]: Samplers with indices corresponding to the sampled textures
- [[buffer]]: Uniform buffers, followed by storage buffers. Vertex buffer 0
  is bound at [[buffer(14)]], vertex buffer 1 at [[buffer(15)]], and so on.
  Rather than manually authoring vertex buffer indices, use the
  [[stage_in]] attribute which will automatically use the vertex input
  information from the [SDL_GPUPipeline](SDL_GPUPipeline).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)
- [SDL_ReleaseGPUShader](SDL_ReleaseGPUShader)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

