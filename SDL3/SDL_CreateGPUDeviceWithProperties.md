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
- [`SDL_PROP_GPU_DEVICE_CREATE_FEATURE_CLIP_DISTANCE_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_FEATURE_CLIP_DISTANCE_BOOLEAN):
  Enable Vulkan device feature shaderClipDistance. If disabled, clip
  distances are not supported in shader code: gl_ClipDistance[] built-ins
  of GLSL, SV_ClipDistance0/1 semantics of HLSL and [[clip_distance]]
  attribute of Metal. Disabling optional features allows the application to
  run on some older Android devices. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_FEATURE_DEPTH_CLAMPING_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_FEATURE_DEPTH_CLAMPING_BOOLEAN):
  Enable Vulkan device feature depthClamp. If disabled, there is no depth
  clamp support and enable_depth_clip in
  [SDL_GPURasterizerState](SDL_GPURasterizerState) must always be set to
  true. Disabling optional features allows the application to run on some
  older Android devices. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_FEATURE_INDIRECT_DRAW_FIRST_INSTANCE_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_FEATURE_INDIRECT_DRAW_FIRST_INSTANCE_BOOLEAN):
  Enable Vulkan device feature drawIndirectFirstInstance. If disabled, the
  argument first_instance of
  [SDL_GPUIndirectDrawCommand](SDL_GPUIndirectDrawCommand) must be set to
  zero. Disabling optional features allows the application to run on some
  older Android devices. Defaults to true.
- [`SDL_PROP_GPU_DEVICE_CREATE_FEATURE_ANISOTROPY_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_FEATURE_ANISOTROPY_BOOLEAN):
  Enable Vulkan device feature samplerAnisotropy. If disabled,
  enable_anisotropy of [SDL_GPUSamplerCreateInfo](SDL_GPUSamplerCreateInfo)
  must be set to false. Disabling optional features allows the application
  to run on some older Android devices. Defaults to true.

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
- [`SDL_PROP_GPU_DEVICE_CREATE_D3D12_ALLOW_FEWER_RESOURCE_SLOTS_BOOLEAN`](SDL_PROP_GPU_DEVICE_CREATE_D3D12_ALLOW_FEWER_RESOURCE_SLOTS_BOOLEAN):
  By default, Resourcing Binding Tier 2 is required for D3D12 support.
  However, an application can set this property to true to enable Tier 1
  support, if (and only if) the application uses 8 or fewer storage
  resources across all shader stages. As of writing, this property is
  useful for targeting Intel Haswell and Broadwell GPUs; other hardware
  either supports Tier 2 Resource Binding or does not support D3D12 in any
  capacity. Defaults to false.

With the Vulkan renderer: -
[`SDL_PROP_GPU_DEVICE_CREATE_VULKAN_REQUIRE_HARDWARE_ACCELERATION`](SDL_PROP_GPU_DEVICE_CREATE_VULKAN_REQUIRE_HARDWARE_ACCELERATION):
By default, Vulkan device enumeration includes drivers of all types,
including software renderers (for example, the Lavapipe Mesa driver). This
can be useful if your application _requires_ [SDL_GPU](SDL_GPU), but if you
can provide your own fallback renderer (for example, an OpenGL renderer)
this property can be set to true. Defaults to false.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGPUShaderFormats](SDL_GetGPUShaderFormats)
- [SDL_GetGPUDeviceDriver](SDL_GetGPUDeviceDriver)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)
- [SDL_GPUSupportsProperties](SDL_GPUSupportsProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

