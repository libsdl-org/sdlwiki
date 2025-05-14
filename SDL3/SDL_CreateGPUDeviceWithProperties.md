# SDL_CreateGPUDeviceWithProperties

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUDevice * SDL_CreateGPUDeviceWithProperties(
    SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_GPUDevice](SDL_GPUDevice) *) Returns a GPU context on success or NULL
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

- [`SDL_PROP_GPU_DEVICE_CREATE_DEBUGMODE_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_DEBUGMODE_BOOLEAN):
  enable debug mode properties and validations, defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_PREFERLOWPOWER_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_PREFERLOWPOWER_BOOLEAN):
  enable to prefer energy efficiency over maximum GPU performance, defaults
  to false.
- [`SDL_PROP_GPU_DEVICE_CREATE_VERBOSE_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_VERBOSE_BOOLEAN):
  enable to automatically log useful debug information on device creation,
  defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_NAME_STRING`](SDL_PROP_GPU_DEVICE_CREATE_NAME_STRING):
  the name of the GPU driver to use, if a specific one is desired.

These are the current shader format properties:

- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_PRIVATE_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_PRIVATE_BOOLEAN):
  The app is able to provide shaders for an NDA platform.
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_SPIRV_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_SPIRV_BOOLEAN):
  The app is able to provide SPIR-V shaders if applicable.
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXBC_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXBC_BOOLEAN):
  The app is able to provide DXBC shaders if applicable
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXIL_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXIL_BOOLEAN):
  The app is able to provide DXIL shaders if applicable.
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_MSL_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_MSL_BOOLEAN):
  The app is able to provide MSL shaders if applicable.
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_METALLIB_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_METALLIB_BOOLEAN):
  The app is able to provide Metal shader libraries if applicable.

With the D3D12 renderer:

- [`SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING`](SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING):
  the prefix to use for all vertex semantics, default is "TEXCOORD".

With the Vulkan renderer:

- [`SDL_PROP_GPU_DEVICE_CREATE_VULKAN_SHADERCLIPDISTANCE_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_VULKAN_SHADERCLIPDISTANCE_BOOL):
  Enable device feature shaderClipDistance. If disabled, clip distances are
  not supported in shader code: gl_ClipDistance[] built-ins of GLSL,
  SV_ClipDistance0/1 semantics of HLSL and [[clip_distance]] attribute of
  Metal. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_VULKAN_DEPTHCLAMP_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_VULKAN_DEPTHCLAMP_BOOL):
  Enable device feature depthClamp. If disabled, there is no depth clamp
  support and enable_depth_clip in
  [SDL_GPURasterizerState](SDL_GPURasterizerState) must always be set to
  true. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_VULKAN_DRAWINDIRECTFIRST_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_VULKAN_DRAWINDIRECTFIRST_BOOL):
  Enable device feature drawIndirectFirstInstance. If disabled, the
  argument first_instance of
  [SDL_GPUIndirectDrawCommand](SDL_GPUIndirectDrawCommand) must be set to
  zero. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_VULKAN_SAMPLERANISOTROPY_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_VULKAN_SAMPLERANISOTROPY_BOOL):
  Enable device feature samplerAnisotropy. If disabled, enable_anisotropy
  of [SDL_GPUSamplerCreateInfo](SDL_GPUSamplerCreateInfo) must be set to
  false. Defaults to true.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGPUShaderFormats](SDL_GetGPUShaderFormats)
- [SDL_GetGPUDeviceDriver](SDL_GetGPUDeviceDriver)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)
- [SDL_GPUSupportsProperties](SDL_GPUSupportsProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

