###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CancelGPUCommandBuffer

Cancels a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_CancelGPUCommandBuffer(
    SDL_GPUCommandBuffer *command_buffer);
```

## Function Parameters

|                                                |                    |                   |
| ---------------------------------------------- | ------------------ | ----------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer. |

## Return Value

(bool) Returns true on success, false on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

None of the enqueued commands are executed.

It is an error to call this function after a swapchain texture has been
acquired.

This must be called from the thread the command buffer was acquired on.

You must not reference the command buffer after calling this function.

## Version

This function is available since SDL 3.1.6.

## See Also

- [SDL_WaitAndAcquireSwapchainTexture](SDL_WaitAndAcquireSwapchainTexture)
- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

