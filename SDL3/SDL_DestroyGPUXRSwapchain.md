# SDL_DestroyGPUXRSwapchain

Destroys and OpenXR swapchain previously returned by [SDL_CreateGPUXRSwapchain](SDL_CreateGPUXRSwapchain).

## Header File

Defined in [<SDL3/SDL_openxr.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_openxr.h)

## Syntax

```c
XrResult SDL_DestroyGPUXRSwapchain(SDL_GPUDevice *device, XrSwapchain swapchain, SDL_GPUTexture **swapchainImages);
```

## Function Parameters

|                                     |                     |                                                                                                                 |
| ----------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *    | **device**          | a GPU context.                                                                                                  |
| XrSwapchain                         | **swapchain**       | a swapchain previously returned by [SDL_CreateGPUXRSwapchain](SDL_CreateGPUXRSwapchain).                        |
| [SDL_GPUTexture](SDL_GPUTexture) ** | **swapchainImages** | an array of swapchain images returned by the same call to [SDL_CreateGPUXRSwapchain](SDL_CreateGPUXRSwapchain). |

## Return Value

(XrResult) Returns the result of the call.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)
- [SDL_CreateGPUXRSession](SDL_CreateGPUXRSession)
- [SDL_CreateGPUXRSwapchain](SDL_CreateGPUXRSwapchain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryOpenxr](CategoryOpenxr)

