###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WaitAndAcquireGPUSwapchainTexture

Blocks the thread until a swapchain texture is available to be acquired, and then acquires it.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_WaitAndAcquireGPUSwapchainTexture(
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
buffer used to acquire it. It is an error to call
[SDL_CancelGPUCommandBuffer](SDL_CancelGPUCommandBuffer)() after a
swapchain texture is acquired.

The swapchain texture is managed by the implementation and must not be
freed by the user. You MUST NOT call this function from any thread other
than the one that created the window.

## Thread Safety

This function should only be called from the thread that created the
window.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

