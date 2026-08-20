# SDL_CreateGPUShader

Creates a shader to be used when creating a graphics pipeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUShader * SDL_CreateGPUShader(
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

Shader resource bindings must be authored to follow a particular convention
depending on the shader format. See below for details.

---

**SPIR-V (GLSL)**

For vertex shaders, use: - Set 0 for samplers, storage textures, and
storage buffers - Set 1 for uniform data

For fragment shaders, use: - Set 2 for samplers, storage textures, and
storage buffers - Set 3 for uniform data

The first resource in a given set must have a `binding` of 0. Additional
resources must appear at consecutive bindings (1, 2, etc), leaving no gaps
in the set.

All samplers must come first in the binding order, in order of how they are
bound via `SDL_BindGPU*Samplers()`.

All storage textures must come after all samplers in the binding order, in
order of how they are bound via `SDL_Bind*StorageTextures()`.

All storage buffers must come after all storage textures in the binding
order, in order of how they are bound via `SDL_Bind*StorageBuffers()`.

**Example**

If a vertex shader binds 2 samplers, 2 storage textures, 2 storage buffers,
and 2 uniform buffers, its binding layout should look like this:

```glsl
// Any samplers come first in the set, in SDL bind slot order
layout(set = 0, binding = 0) uniform sampler2D samplerBoundToSlot0;
layout(set = 0, binding = 1) uniform sampler2D samplerBoundToSlot1;
// Any storage textures come next in the set, in SDL bind slot order
layout(set = 0, binding = 2) uniform image2D storageTextureBoundToSlot0;
layout(set = 0, binding = 3) uniform image2D storageTextureBoundToSlot1;
// Any storage buffers come next in the set, in SDL bind slot order
layout(set = 0, binding = 4) buffer storageBufferBoundToSlot0 { ... };
layout(set = 0, binding = 5) buffer storageBufferBoundToSlot1 { ... };
// Any uniform buffers are in their own set, in SDL slot order
layout(set = 1, binding = 0) uniform UniformDataBoundToSlot0 { ... };
layout(set = 1, binding = 1) uniform UniformDataBoundToSlot1 { ... };
```

---

**DXBC / DXIL (HLSL)**

For vertex shaders, use: - `(t[n], space0)` for sampled textures, storage
textures, and storage buffers - `(s[n], space0)` for samplers - `(b[n],
space1)` for uniform data

For fragment (aka "pixel") shaders, use: - `(t[n], space2)` for sampled
textures, storage textures, and storage buffers - `(s[n], space2)` for
samplers - `(b[n], space3)` for uniform data

The first resource in a given register set must have a register index of
`0`. Additional resources must appear at consecutive indices (1, 2, etc),
leaving no gaps in the register set.

All sampled textures must come first in the `t` register set, in order of
how they are bound via `SDL_BindGPU*Samplers()`.

All sampler objects must be in the `s` register set, in the same order as
the textures above.

All storage textures must come after all samplers in the `t` register set,
in order of how they are bound via `SDL_Bind*StorageTextures()`.

All storage buffers must come after all storage textures in the `t`
register set, in order of how they are bound via
`SDL_Bind*StorageBuffers()`.

**Example**

If a pixel shader binds 2 samplers, 2 storage textures, 2 storage buffers,
and 2 uniform buffers, its binding layout should look like this:

```c
// Any samplers and sampled textures come first in their respective register sets, in SDL bind slot order
SamplerState SamplerBoundToSlot0 : register( s0, space2 );
SamplerState SamplerBoundToSlot1 : register( s1, space2 );
Texture2D SampledTextureBoundToSlot0 : register( t0, space2 );
Texture2D SampledTextureBoundToSlot1 : register( t1, space2 );
// Any storage textures come next in the `t` register set, in SDL bind slot order
Texture2D StorageTextureBoundToSlot0 : register( t2, space2 );
Texture2D StorageTextureBoundToSlot1 : register( t3, space2 );
// Any storage buffers come next in the `t` register set, in SDL bind slot order
ByteAddressBuffer StorageBufferBoundToSlot0 : register( t4, space2 );
ByteAddressBuffer StorageBufferBoundToSlot1 : register( t5, space2 );
// Any uniform buffers are in the `b` register set *and* in their own space, in SDL slot order
cbuffer UniformDataBoundToSlot0 : register( b0, space3 ) { ... };
cbuffer UniformDataBoundToSlot1 : register( b1, space3 ) { ... };
```

---

**MSL / Metallib (Metal Shading Language)**

The first resource in a given argument table must have an index of `0`.
Additional resources must appear at consecutive indices (1, 2, etc),
leaving no gaps in the table. (_Except_ in the case of vertex buffers,
which are mentioned below.)

All sampled textures must come first in the `[[texture]]` argument table,
in order of how they are bound via `SDL_BindGPU*Samplers()`.

All sampler objects must be in the `[[sampler]]` argument table, in the
same order as the textures above.

All storage textures must come after all sampled textures in the
`[[texture]]` argument table, in order of how they are bound via
`SDL_BindGPU*StorageTextures()`.

All uniform buffers must come first in the `[[buffer]]` argument table, in
order of their slots in `SDL_PushGPU*UniformData()`.

All storage buffers must come after all uniform buffers in the `[[buffer]]`
argument table, in order of how they are bound via
`SDL_BindGPU*StorageBuffers()`.

In Metal, vertex buffers are also included in the `[[buffer]]` argument
table. To work around this, SDL forces the vertex buffer bound to slot 0 to
be bound at `[[buffer(14)]]`. The vertex buffer in slot 1 will be bound to
`[[buffer(15)]]`, and so on. Rather than manually authoring vertex buffer
indices, use the `[[stage_in]]` attribute which will automatically use the
vertex input information from the
[SDL_GPUGraphicsPipeline](SDL_GPUGraphicsPipeline).

**Example**

For a vertex shader with 1 vertex buffer, 2 samplers, 2 storage textures, 2
storage buffers, and 2 uniform buffers, the main function signature should
look something like this:

```c++
vertex VertexOutput ExampleVertexShader(
    // Vertex buffers are their own special thing...
    SomeVertexInput input [[stage_in]], // alternatively, SomeVertexInput input [[buffer(14)]]
    // Any samplers go in the `sampler` table, in SDL bind slot order
    sampler samplerBoundToSlot0 [[sampler(0)]],
    sampler samplerBoundToSlot1 [[sampler(1)]],
    // Any sampled textures come first in the `texture` table, in SDL bind slot order
    texture2d<float> sampledTextureBoundToSlot0 [[texture(0)]],
    texture2d<float> sampledTextureBoundToSlot1 [[texture(1)]],
    // Any storage textures come next in the `texture` table, in SDL bind slot order
    texture2d<float> storageTextureBoundToSlot0 [[texture(2)]],
    texture2d<float> storageTextureBoundToSlot1 [[texture(3)]],
    // Any uniform buffers come first in the `buffer` table, in SDL slot order
    constant SomeUniformStruct uniformDataBoundToSlot0 [[buffer(0)]],
    constant SomeUniformStruct uniformDataBoundToSlot1 [[buffer(1)]],
    // Any storage buffers come next in the `buffer` table, in SDL bind slot order
    device SomeBufferStruct& storageBufferBoundToSlot0 [[buffer(2)]],
    device SomeBufferStruct& storageBufferBoundToSlot1 [[buffer(3)]]);

```

---

Shader semantics other than system-value semantics do not matter in D3D12.
For ease of use, the SDL implementation assumes that non system-value
semantics will all be `TEXCOORD`. If you are using HLSL as the shader
source language, your vertex semantics should start at `TEXCOORD0` and
increment like so: `TEXCOORD1`, `TEXCOORD2`, etc.

If you wish to change the semantic prefix to something other than
`TEXCOORD` you can use
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
