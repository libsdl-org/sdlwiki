###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuTransferBuffer

Creates a transfer buffer to be used when uploading to or downloading from graphics resources.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuTransferBuffer* SDL_CreateGpuTransferBuffer(
    SDL_GpuDevice *device,
    SDL_GpuTransferBufferCreateInfo *transferBufferCreateInfo);
```

## Function Parameters

|                                                                      |                              |                                                                 |
| -------------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                                     | **device**                   | a GPU Context.                                                  |
| [SDL_GpuTransferBufferCreateInfo](SDL_GpuTransferBufferCreateInfo) * | **transferBufferCreateInfo** | a struct describing the state of the transfer buffer to create. |

## Return Value

([SDL_GpuTransferBuffer](SDL_GpuTransferBuffer) *) Returns a transfer
buffer on success, or NULL on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UploadToGpuBuffer](SDL_UploadToGpuBuffer)
- [SDL_DownloadFromGpuBuffer](SDL_DownloadFromGpuBuffer)
- [SDL_UploadToGpuTexture](SDL_UploadToGpuTexture)
- [SDL_DownloadFromGpuTexture](SDL_DownloadFromGpuTexture)
- [SDL_ReleaseGpuTransferBuffer](SDL_ReleaseGpuTransferBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

