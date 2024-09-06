###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireGPUSwapchainTexture

Acquire a texture to use in presentation.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTexture* SDL_AcquireGPUSwapchainTexture(
    SDL_GPUCommandBuffer *command_buffer,
    SDL_Window *window,
    Uint32 *w,
    Uint32 *h);
```

## Function Parameters

|                                                |                    |                                                |
| ---------------------------------------------- | ------------------ | ---------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                              |
| [SDL_Window](SDL_Window) *                     | **window**         | a window that has been claimed.                |
| Uint32 *                                       | **w**              | a pointer filled in with the swapchain width.  |
| Uint32 *                                       | **h**              | a pointer filled in with the swapchain height. |

## Return Value

([SDL_GPUTexture](SDL_GPUTexture) *) Returns a swapchain texture.

## Remarks

When a swapchain texture is acquired on a command buffer, it will
automatically be submitted for presentation when the command buffer is
submitted. The swapchain texture should only be referenced by the command
buffer used to acquire it. May return NULL under certain conditions. This
is not necessarily an error. This texture is managed by the implementation
and must not be freed by the user. You MUST NOT call this function from any
thread other than the one that created the window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ClaimWindowForGPUDevice](SDL_ClaimWindowForGPUDevice)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

