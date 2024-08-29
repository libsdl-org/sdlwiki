###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnmapGpuTransferBuffer

Unmaps a previously mapped transfer buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UnmapGpuTransferBuffer(
    SDL_GpuDevice *device,
    SDL_GpuTransferBuffer *transferBuffer);
```

## Function Parameters

|                                                  |                    |                                      |
| ------------------------------------------------ | ------------------ | ------------------------------------ |
| [SDL_GpuDevice](SDL_GpuDevice) *                 | **device**         | a GPU context.                       |
| [SDL_GpuTransferBuffer](SDL_GpuTransferBuffer) * | **transferBuffer** | a previously mapped transfer buffer. |

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

