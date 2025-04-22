# SDL_CreateGPUDevice

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUDevice * SDL_CreateGPUDevice(
    SDL_GPUShaderFormat format_flags,
    bool debug_mode,
    const char *name);
```

## Function Parameters

|                                            |                  |                                                                       |
| ------------------------------------------ | ---------------- | --------------------------------------------------------------------- |
| [SDL_GPUShaderFormat](SDL_GPUShaderFormat) | **format_flags** | a bitflag indicating which shader formats the app is able to provide. |
| bool                                       | **debug_mode**   | enable debug mode properties and validations.                         |
| const char *                               | **name**         | the preferred GPU driver, or NULL to let SDL pick the optimal driver. |

## Return Value

([SDL_GPUDevice](SDL_GPUDevice) *) Returns a GPU context on success or NULL
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The GPU driver name can be one of the following:

- "vulkan": [Vulkan](CategoryGPU#vulkan)
- "direct3d12": [D3D12](CategoryGPU#d3d12)
- "metal": [Metal](CategoryGPU#metal)
- NULL: let SDL pick the optimal driver

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)
- [SDL_GetGPUShaderFormats](SDL_GetGPUShaderFormats)
- [SDL_GetGPUDeviceDriver](SDL_GetGPUDeviceDriver)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)
- [SDL_GPUSupportsShaderFormats](SDL_GPUSupportsShaderFormats)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

