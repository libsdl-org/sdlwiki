###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUDeviceWithProperties

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUDevice* SDL_CreateGPUDeviceWithProperties(
    SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_GPUDevice](SDL_GPUDevice) *) Returns a GPU context on success or NULL
on failure.

## Remarks

These are the supported properties:

- [`SDL_PROP_GPU_DEVICE_CREATE_DEBUGMODE_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_DEBUGMODE_BOOL):
  enable debug mode properties and validations, defaults to
  [SDL_TRUE](SDL_TRUE).
- [`SDL_PROP_GPU_DEVICE_CREATE_PREFERLOWPOWER_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_PREFERLOWPOWER_BOOL):
  enable to prefer energy efficiency over maximum GPU performance, defaults
  to [SDL_FALSE](SDL_FALSE).
- [`SDL_PROP_GPU_DEVICE_CREATE_NAME_STRING`](SDL_PROP_GPU_DEVICE_CREATE_NAME_STRING):
  the name of the GPU driver to use, if a specific one is desired.

These are the current shader format properties:

- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_PRIVATE_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_PRIVATE_BOOL):
  The app is able to provide shaders for an NDA platform.
- [`SDL_PROP_GPU_DEVICE_CREATE_SHADERS_SPIRV_BOOL`](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_SPIRV_BOOL):
  The app is able to provide SPIR-V shaders if applicable.
- [SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXBC_BOOL](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXBC_BOOL)`:
  The app is able to provide DXBC shaders if applicable
  `[SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXIL_BOOL](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXIL_BOOL)`:
  The app is able to provide DXIL shaders if applicable.
- `[SDL_PROP_GPU_DEVICE_CREATE_SHADERS_MSL_BOOL](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_MSL_BOOL)`:
  The app is able to provide MSL shaders if applicable.
- `[SDL_PROP_GPU_DEVICE_CREATE_SHADERS_METALLIB_BOOL](SDL_PROP_GPU_DEVICE_CREATE_SHADERS_METALLIB_BOOL)`:
  The app is able to provide Metal shader libraries if applicable.

With the D3D12 renderer:

- `[SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING](SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING)`:
  the prefix to use for all vertex semantics, default is "TEXCOORD".

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGPUDriver](SDL_GetGPUDriver)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

