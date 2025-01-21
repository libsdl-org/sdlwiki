###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MapGPUTransferBuffer

Maps a transfer buffer into application address space.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void* SDL_MapGPUTransferBuffer(
    SDL_GPUDevice *device,
    SDL_GPUTransferBuffer *transfer_buffer,
    bool cycle);
```

## Function Parameters

|                                                  |                     |                                                             |
| ------------------------------------------------ | ------------------- | ----------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                 | **device**          | a GPU context.                                              |
| [SDL_GPUTransferBuffer](SDL_GPUTransferBuffer) * | **transfer_buffer** | a transfer buffer.                                          |
| bool                                             | **cycle**           | if true, cycles the transfer buffer if it is already bound. |

## Return Value

(void *) Returns the address of the mapped transfer buffer memory, or NULL
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

You must unmap the transfer buffer before encoding upload commands.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

