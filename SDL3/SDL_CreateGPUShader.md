###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

For DXBC and DXIL shaders, use the following register order:

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
  information from the [SDL_GPUGraphicsPipeline](SDL_GPUGraphicsPipeline).

Shader semantics other than system-value semantics do not matter in D3D12
and for ease of use the SDL implementation assumes that non system-value
semantics will all be TEXCOORD. If you are using HLSL as the shader source
language, your vertex semantics should start at TEXCOORD0 and increment
like so: TEXCOORD1, TEXCOORD2, etc. If you wish to change the semantic
prefix to something other than TEXCOORD you can use
[SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING](SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING)
with
[SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)().

There are optional properties that can be provided through `props`. These
are the supported properties:

- [`SDL_PROP_GPU_SHADER_CREATE_NAME_STRING`](SDL_PROP_GPU_SHADER_CREATE_NAME_STRING):
  a name that can be displayed in debugging tools.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)
- [SDL_ReleaseGPUShader](SDL_ReleaseGPUShader)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

