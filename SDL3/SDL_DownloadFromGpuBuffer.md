###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DownloadFromGpuBuffer

Copies data from a buffer to a transfer buffer on the GPU timeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DownloadFromGpuBuffer(
    SDL_GpuCopyPass *copyPass,
    SDL_GpuBufferRegion *source,
    SDL_GpuTransferBufferLocation *destination);
```

## Function Parameters

|                                                                  |                 |                                              |
| ---------------------------------------------------------------- | --------------- | -------------------------------------------- |
| [SDL_GpuCopyPass](SDL_GpuCopyPass) *                             | **copyPass**    | a copy pass handle.                          |
| [SDL_GpuBufferRegion](SDL_GpuBufferRegion) *                     | **source**      | the source buffer with offset and size.      |
| [SDL_GpuTransferBufferLocation](SDL_GpuTransferBufferLocation) * | **destination** | the destination transfer buffer with offset. |

## Remarks

This data is not guaranteed to be copied until the command buffer fence is
signaled.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


