###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AcquireGpuSwapchainTexture

Acquire a texture to use in presentation.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuTexture* SDL_AcquireGpuSwapchainTexture(
    SDL_GpuCommandBuffer *commandBuffer,
    SDL_Window *window,
    Uint32 *pWidth,
    Uint32 *pHeight);
```

## Function Parameters

|                                                |                   |                                                |
| ---------------------------------------------- | ----------------- | ---------------------------------------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer.                              |
| [SDL_Window](SDL_Window) *                     | **window**        | a window that has been claimed.                |
| Uint32 *                                       | **pWidth**        | a pointer filled in with the swapchain width.  |
| Uint32 *                                       | **pHeight**       | a pointer filled in with the swapchain height. |

## Return Value

([SDL_GpuTexture](SDL_GpuTexture) *) Returns a swapchain texture.

## Remarks

When a swapchain texture is acquired on a command buffer, it will
automatically be submitted for presentation when the command buffer is
submitted. The swapchain texture should only be referenced by the command
buffer used to acquire it. May return NULL under certain conditions. This
is not necessarily an error. This texture is managed by the implementation
and must not be freed by the user. You MUST NOT call this function from any
thread other than the one that created the window.

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_ClaimGpuWindow](SDL_ClaimGpuWindow)
- [SDL_SubmitGpu](SDL_SubmitGpu)
- [SDL_SubmitGpuAndAcquireFence](SDL_SubmitGpuAndAcquireFence)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

