# SDL_AcquireGPUSwapchainTexture

Acquire a texture to use in presentation.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_AcquireGPUSwapchainTexture(
    SDL_GPUCommandBuffer *command_buffer,
    SDL_Window *window,
    SDL_GPUTexture **swapchain_texture,
    Uint32 *swapchain_texture_width,
    Uint32 *swapchain_texture_height);
```

## Function Parameters

|                                                |                              |                                                                     |
| ---------------------------------------------- | ---------------------------- | ------------------------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer**           | a command buffer.                                                   |
| [SDL_Window](SDL_Window) *                     | **window**                   | a window that has been claimed.                                     |
| [SDL_GPUTexture](SDL_GPUTexture) **            | **swapchain_texture**        | a pointer filled in with a swapchain texture handle.                |
| [Uint32](Uint32) *                             | **swapchain_texture_width**  | a pointer filled in with the swapchain texture width, may be NULL.  |
| [Uint32](Uint32) *                             | **swapchain_texture_height** | a pointer filled in with the swapchain texture height, may be NULL. |

## Return Value

(bool) Returns true on success, false on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When a swapchain texture is acquired on a command buffer, it will
automatically be submitted for presentation when the command buffer is
submitted. The swapchain texture should only be referenced by the command
buffer used to acquire it.

This function will fill the swapchain texture handle with NULL if too many
frames are in flight. This is not an error.

If you use this function, it is possible to create a situation where many
command buffers are allocated while the rendering context waits for the GPU
to catch up, which will cause memory usage to grow. You should use
[SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)()
unless you know what you are doing with timing.

The swapchain texture is managed by the implementation and must not be
freed by the user. You MUST NOT call this function from any thread other
than the one that created the window.

## Thread Safety

This function should only be called from the thread that created the
window.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ClaimWindowForGPUDevice](SDL_ClaimWindowForGPUDevice)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)
- [SDL_CancelGPUCommandBuffer](SDL_CancelGPUCommandBuffer)
- [SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)
- [SDL_WaitForGPUSwapchain](SDL_WaitForGPUSwapchain)
- [SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)
- [SDL_SetGPUAllowedFramesInFlight](SDL_SetGPUAllowedFramesInFlight)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

