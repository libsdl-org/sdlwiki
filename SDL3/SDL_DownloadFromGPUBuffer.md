###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DownloadFromGPUBuffer

Copies data from a buffer to a transfer buffer on the GPU timeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DownloadFromGPUBuffer(
    SDL_GPUCopyPass *copyPass,
    SDL_GPUBufferRegion *source,
    SDL_GPUTransferBufferLocation *destination);
```

## Function Parameters

|                                                                  |                 |                                              |
| ---------------------------------------------------------------- | --------------- | -------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                             | **copyPass**    | a copy pass handle.                          |
| [SDL_GPUBufferRegion](SDL_GPUBufferRegion) *                     | **source**      | the source buffer with offset and size.      |
| [SDL_GPUTransferBufferLocation](SDL_GPUTransferBufferLocation) * | **destination** | the destination transfer buffer with offset. |

## Remarks

This data is not guaranteed to be copied until the command buffer fence is
signaled.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

