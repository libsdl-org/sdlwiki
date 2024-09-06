###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUTransferBuffer

Creates a transfer buffer to be used when uploading to or downloading from graphics resources.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTransferBuffer* SDL_CreateGPUTransferBuffer(
    SDL_GPUDevice *device,
    const SDL_GPUTransferBufferCreateInfo *createinfo);
```

## Function Parameters

|                                                                            |                |                                                                 |
| -------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                                           | **device**     | a GPU Context.                                                  |
| const [SDL_GPUTransferBufferCreateInfo](SDL_GPUTransferBufferCreateInfo) * | **createinfo** | a struct describing the state of the transfer buffer to create. |

## Return Value

([SDL_GPUTransferBuffer](SDL_GPUTransferBuffer) *) Returns a transfer
buffer on success, or NULL on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UploadToGPUBuffer](SDL_UploadToGPUBuffer)
- [SDL_DownloadFromGPUBuffer](SDL_DownloadFromGPUBuffer)
- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)
- [SDL_ReleaseGPUTransferBuffer](SDL_ReleaseGPUTransferBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

