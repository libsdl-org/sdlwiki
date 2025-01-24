# SDL_ReleaseGPUTransferBuffer

Frees the given transfer buffer as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGPUTransferBuffer(
    SDL_GPUDevice *device,
    SDL_GPUTransferBuffer *transfer_buffer);
```

## Function Parameters

|                                                  |                     |                                    |
| ------------------------------------------------ | ------------------- | ---------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                 | **device**          | a GPU context.                     |
| [SDL_GPUTransferBuffer](SDL_GPUTransferBuffer) * | **transfer_buffer** | a transfer buffer to be destroyed. |

## Remarks

You must not reference the transfer buffer after calling this function.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

