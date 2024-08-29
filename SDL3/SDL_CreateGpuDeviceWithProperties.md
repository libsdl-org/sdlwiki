###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuDeviceWithProperties

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuDevice* SDL_CreateGpuDeviceWithProperties(
    SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_GpuDevice](SDL_GpuDevice) *) Returns a GPU context on success or NULL
on failure.

## Remarks

These are the supported properties:

- [`SDL_PROP_GPU_CREATEDEVICE_DEBUGMODE_BOOL`](SDL_PROP_GPU_CREATEDEVICE_DEBUGMODE_BOOL):
  enable debug mode properties and validations, default is true
- [`SDL_PROP_GPU_CREATEDEVICE_PREFERLOWPOWER_BOOL`](SDL_PROP_GPU_CREATEDEVICE_PREFERLOWPOWER_BOOL):
  enable to prefer energy efficiency over maximum GPU performance
- [`SDL_PROP_GPU_CREATEDEVICE_NAME_STRING`](SDL_PROP_GPU_CREATEDEVICE_NAME_STRING):
  the name of the GPU driver to use, if a specific one is desired

These are the current shader format properties:

[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_SECRET_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_SECRET_BOOL):
The app is able to provide shaders for an NDA platform
[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_SPIRV_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_SPIRV_BOOL):
The app is able to provide SPIR-V shaders if applicable
[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_DXBC_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_DXBC_BOOL):
The app is able to provide DXBC shaders if applicable
[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_DXIL_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_DXIL_BOOL):
The app is able to provide DXIL shaders if applicable
[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_MSL_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_MSL_BOOL):
The app is able to provide MSL shaders if applicable
[`SDL_PROP_GPU_CREATEDEVICE_SHADERS_METALLIB_BOOL`](SDL_PROP_GPU_CREATEDEVICE_SHADERS_METALLIB_BOOL):
The app is able to provide Metal shader libraries if applicable

With the D3D12 renderer: -
[`SDL_PROP_GPU_CREATEDEVICE_D3D12_SEMANTIC_NAME_STRING`](SDL_PROP_GPU_CREATEDEVICE_D3D12_SEMANTIC_NAME_STRING):
the prefix to use for all vertex semantics, default is "TEXCOORD"

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_GetGpuDriver](SDL_GetGpuDriver)
- [SDL_DestroyGpuDevice](SDL_DestroyGpuDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

