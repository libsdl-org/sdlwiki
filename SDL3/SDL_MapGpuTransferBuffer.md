###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MapGpuTransferBuffer

Maps a transfer buffer into application address space.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void* SDL_MapGpuTransferBuffer(
    SDL_GpuDevice *device,
    SDL_GpuTransferBuffer *transferBuffer,
    SDL_bool cycle);
```

## Function Parameters

|                                                  |                    |                                                                     |
| ------------------------------------------------ | ------------------ | ------------------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                 | **device**         | a GPU context.                                                      |
| [SDL_GpuTransferBuffer](SDL_GpuTransferBuffer) * | **transferBuffer** | a transfer buffer.                                                  |
| [SDL_bool](SDL_bool)                             | **cycle**          | if [SDL_TRUE](SDL_TRUE), cycles the transfer buffer if it is bound. |

## Return Value

(void *) Returns the address of the mapped transfer buffer memory.

## Remarks

You must unmap the transfer buffer before encoding upload commands.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

