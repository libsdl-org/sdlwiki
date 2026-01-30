# SDL_CreateGPUXRSwapchain

Creates an OpenXR swapchain.

## Header File

Defined in [<SDL3/SDL_openxr.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_openxr.h)

## Syntax

```c
XrResult SDL_CreateGPUXRSwapchain(
    SDL_GPUDevice *device,
    XrSession session,
    const XrSwapchainCreateInfo *createinfo, 
    SDL_GPUTextureFormat format,
    XrSwapchain *swapchain,
    SDL_GPUTexture ***textures);
```

## Function Parameters

|                                              |                |                                                                 |
| -------------------------------------------- | -------------- | --------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *             | **device**     | a GPU context.                                                  |
| XrSession                                    | **session**    | an OpenXR session created for the given device.                 |
| const XrSwapchainCreateInfo *                | **createinfo** | the create info for the OpenXR swapchain, sans the format.      |
| [SDL_GPUTextureFormat](SDL_GPUTextureFormat) | **format**     | a supported format for the OpenXR swapchain.                    |
| XrSwapchain *                                | **swapchain**  | a pointer filled in with the created OpenXR swapchain.          |
| [SDL_GPUTexture](SDL_GPUTexture) ***         | **textures**   | a pointer filled in with the array of created swapchain images. |

## Return Value

(XrResult) Returns the result of the call.

## Remarks

The array returned via `textures` is sized according to
`xrEnumerateSwapchainImages`, and thus should only be accessed via index
values returned from `xrAcquireSwapchainImage`.

Applications are still allowed to call `xrEnumerateSwapchainImages` on the
returned XrSwapchain if they need to get the exact size of the array.

## See Also

- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)
- [SDL_CreateGPUXRSession](SDL_CreateGPUXRSession)
- [SDL_GetGPUXRSwapchainFormats](SDL_GetGPUXRSwapchainFormats)
- [SDL_DestroyGPUXRSwapchain](SDL_DestroyGPUXRSwapchain)

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryOpenxr](CategoryOpenxr)

