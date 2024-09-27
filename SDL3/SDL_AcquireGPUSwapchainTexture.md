###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireGPUSwapchainTexture

Acquire a texture to use in presentation.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_AcquireGPUSwapchainTexture(
    SDL_GPUCommandBuffer *command_buffer,
    SDL_Window *window,
    SDL_GPUTexture **swapchainTexture);
```

## Function Parameters

|                                                |                      |                                                      |
| ---------------------------------------------- | -------------------- | ---------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer**   | a command buffer.                                    |
| [SDL_Window](SDL_Window) *                     | **window**           | a window that has been claimed.                      |
| [SDL_GPUTexture](SDL_GPUTexture) **            | **swapchainTexture** | a pointer filled in with a swapchain texture handle. |

## Return Value

(bool) Returns true on success, false on error.

## Remarks

When a swapchain texture is acquired on a command buffer, it will
automatically be submitted for presentation when the command buffer is
submitted. The swapchain texture should only be referenced by the command
buffer used to acquire it. The swapchain texture handle can be NULL under
certain conditions. This is not necessarily an error. If this function
returns false then there is an error. The swapchain texture is managed by
the implementation and must not be freed by the user. The texture
dimensions will be the width and height of the claimed window. You can
obtain these dimensions by calling
[SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels). You MUST NOT call
this function from any thread other than the one that created the window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ClaimWindowForGPUDevice](SDL_ClaimWindowForGPUDevice)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)
- [SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

