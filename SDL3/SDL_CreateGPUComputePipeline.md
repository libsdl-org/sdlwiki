# SDL_CreateGPUComputePipeline

Creates a pipeline object to be used in a compute workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUComputePipeline * SDL_CreateGPUComputePipeline(
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

Shader resource bindings must be authored to follow a particular convention depending on the shader format. See below for details.

---

**SPIR-V**

For compute shaders, use:

- Set 0 for samplers, read-only storage textures, and read-only storage buffers
- Set 1 for read-write storage textures and read-write storage buffers
- Set 2 for uniform data

The first resource in a given set must have a `binding` of 0. Additional resources must appear at consecutive bindings (1, 2, etc), leaving no gaps in the set.

All samplers must come first in the binding order of Set 0, in order of how they are bound via `SDL_BindGPUComputeSamplers()`.

All read-only storage textures must come after all samplers in the binding order, in order of how they are bound via `SDL_BindGPUComputeStorageTextures()`.

All read-only storage buffers must come after all read-only storage textures in the binding order, in order of how they are bound via `SDL_BindGPUComputeStorageBuffers()`.

All read-write storage textures must come first in the binding order of Set 1, in order of how they are bound via `SDL_BeginGPUComputePass()`.

All read-write storage buffers must come after all read-write storage textures in the binding order, in order of how they are bound via `SDL_BeginGPUComputePass()`.

**Example**

If a compute shader binds 2 of each resource type, its binding layout should look like this:

```glsl
// Any samplers come first in Set 0, in SDL bind slot order
layout(set = 0, binding = 0) sampler2d samplerBoundToSlot0;
layout(set = 0, binding = 1) sampler2d samplerBoundToSlot1;
// Any read-only storage textures come next in Set 0, in SDL bind slot order
layout(set = 0, binding = 2) image2d storageTextureBoundToSlot0;
layout(set = 0, binding = 3) image2d storageTextureBoundToSlot1;
// Any read-only storage buffers come next in Set 0, in SDL bind slot order
layout(set = 0, binding = 4) buffer storageBufferBoundToSlot0;
layout(set = 0, binding = 5) buffer storageBufferBoundToSlot1;
// Any read-write storage textures come first in Set 1, in SDL bind slot order
layout(set = 1, binding = 0) image2d rwStorageTextureBoundToSlot0;
layout(set = 1, binding = 1) image2d rwStorageTextureBoundToSlot1;
// Any read-write storage buffers come next in Set 1, in SDL bind slot order
layout(set = 1, binding = 2) buffer rwStorageBufferBoundToSlot0;
layout(set = 1, binding = 3) buffer rwStorageBufferBoundToSlot1;
// Any uniform buffers are in Set 2, in SDL slot order
layout(set = 2, binding = 0) uniform UniformDataBoundToSlot0 {};
layout(set = 2, binding = 1) uniform UniformDataBoundToSlot1 {};
```

---

**DXBC / DXIL (HLSL)**

For compute shaders, use:
- `(t[n], space0)` for sampled textures, read-only storage textures, and read-only storage buffers
- `(s[n], space0)` for samplers
- `(u[n], space1)` for read-write storage textures and read-write storage buffers
- `(b[n], space2)` for uniform data

The first resource in a given register set must have a register index of `0`. Additional resources must appear at consecutive indices (1, 2, etc), leaving no gaps in the register set.

All sampled textures must come first in the `t` register set, in order of how they are bound via `SDL_BindGPUComputeSamplers()`.

All sampler objects must be in the `s` register set, in the same order as the textures above.

All read-only storage textures must come after all samplers in the `t` register set, in order of how they are bound via `SDL_BindComputeStorageTextures()`.

All read-only storage buffers must come after all storage textures in the `t` register set, in order of how they are bound via `SDL_BindComputeStorageBuffers()`.

All read-write storage textures must come first in the `u` register set in `space1`, in order of how they are bound via `SDL_BeginGPUComputePass()`.

All read-write storage buffers must come after all read-write storage textures in the `u` register set in `space1`, in order of how they are bound via `SDL_BeginGPUComputePass()`.

**Example**

If a compute shader binds 2 of each resource type, the layout should look like this:

```c
// Any samplers and sampled textures come first in their respective register sets, in SDL bind slot order
SamplerState SamplerBoundToSlot0 : register( s0, space0 );
SamplerState SamplerBoundToSlot1 : register( s1, space0 );
Texture2D SampledTextureBoundToSlot0 : register( t0, space0 );
Texture2D SampledTextureBoundToSlot1 : register( t1, space0 );
// Any read-only storage textures come next in the `t` register set, in SDL bind slot order
Texture2D StorageTextureBoundToSlot0 : register( t2, space0 );
Texture2D StorageTextureBoundToSlot1 : register( t3, space0 );
// Any read-only storage buffers come next in the `t` register set, in SDL bind slot order
ByteAddressBuffer StorageBufferBoundToSlot0 : register( t4, space0 );
ByteAddressBuffer StorageBufferBoundToSlot1 : register( t5, space0 );
// Any read-write storage textures come first in the `u` register set in space1, in SDL bind slot order
RWTexture2D RWStorageTextureBoundToSlot0 : register( u0, space1 );
RWTexture2D RWStorageTextureBoundToSlot1 : register( u1, space1 );
// Any read-write storage buffers come next in the `u` register set in space1, in SDL bind slot order
RWByteAddressBuffer RWStorageTextureBoundToSlot0 : register( u2, space1 );
RWByteAddressBuffer RWStorageTextureBoundToSlot1 : register( u3, space1 );
// Any uniform buffers are in the `b` register set in space2, in SDL slot order
cbuffer UniformDataBoundToSlot0 : register( b0, space2 ) { ... };
cbuffer UniformDataBoundToSlot1 : register( b1, space2 ) { ... };
```

---

**MSL / Metallib (Metal Shading Language)**

The first resource in a given argument table must have an index of `0`. Additional resources must appear at consecutive indices (1, 2, etc), leaving no gaps in the table.

All sampled textures must come first in the `[[texture]]` argument table, in order of how they are bound via `SDL_BindGPUComputeSamplers()`.

All sampler objects must be in the `[[sampler]]` argument table, in the same order as the textures above.

All read-only storage textures must come after all sampled textures in the `[[texture]]` argument table, in order of how they are bound via `SDL_BindGPUComputeStorageTextures()`.

All read-write storage textures must come after all read-only storage textures in the `[[texture]]` argument table, in order of how they are bound via `SDL_BeginGPUComputePass()`.

All uniform buffers must come first in the `[[buffer]]` argument table, in order of their slots in `SDL_PushGPUComputeUniformData()`.

All read-only storage buffers must come after all uniform buffers in the `[[buffer]]` argument table, in order of how they are bound via `SDL_BindGPUComputeStorageBuffers()`.

All read-write storage buffers must come after all read-only storage buffers in the `[[buffer]]` argument table, in order of how they are bound via `SDL_BeginGPUComputePass()`.

**Example**

For a compute shader binding 2 of each resource type, the main function signature should look like this:

```c++
kernel void ExampleComputeShader(
    // Any samplers go in the `sampler` table, in SDL bind slot order
    sampler samplerBoundToSlot0 [[sampler(0)]],
    sampler samplerBoundToSlot1 [[sampler(1)]],
    // Any sampled textures come first in the `texture` table, in SDL bind slot order
    texture2d<float> sampledTextureBoundToSlot0 [[texture(0)]],
    texture2d<float> sampledTextureBoundToSlot1 [[texture(1)]],
    // Any read-only storage textures come next in the `texture` table, in SDL bind slot order
    texture2d<float> storageTextureBoundToSlot0 [[texture(2)]],
    texture2d<float> storageTextureBoundToSlot1 [[texture(3)]],
    // Any read-write storage textures come next in the `texture` table, in SDL bind slot order
    texture2d<float, access::write> rwStorageTextureBoundToSlot0 [[texture(4)]];
    texture2d<float, access::write> rwStorageTextureBoundToSlot1 [[texture(5)]];
    // Any uniform buffers come first in the `buffer` table, in SDL slot order
    constant SomeUniformStruct uniformDataBoundToSlot0 [[buffer(0)]],
    constant SomeUniformStruct uniformDataBoundToSlot1 [[buffer(1)]],
    // Any read-only storage buffers come next in the `buffer` table, in SDL bind slot order
    device SomeBufferStruct& storageBufferBoundToSlot0 [[buffer(2)]],
    device SomeBufferStruct& storageBufferBoundToSlot1 [[buffer(3)]]);
    // Any read-write storage buffers come next in the `buffer` table, in SDL bind slot order
    device SomeBufferStruct& rwStorageBufferBoundToSlot0 [[buffer(4)]];
    device SomeBufferStruct& rwStorageBufferBoundToSlot1 [[buffer(5)]]);
```

---

There are optional properties that can be provided through `props`. These
are the supported properties:

- [`SDL_PROP_GPU_COMPUTEPIPELINE_CREATE_NAME_STRING`](SDL_PROP_GPU_COMPUTEPIPELINE_CREATE_NAME_STRING):
  a name that can be displayed in debugging tools.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_BindGPUComputePipeline](SDL_BindGPUComputePipeline)
- [SDL_ReleaseGPUComputePipeline](SDL_ReleaseGPUComputePipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

