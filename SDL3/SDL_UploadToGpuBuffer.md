###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UploadToGpuBuffer

Uploads data from a transfer buffer to a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UploadToGpuBuffer(
    SDL_GpuCopyPass *copyPass,
    SDL_GpuTransferBufferLocation *source,
    SDL_GpuBufferRegion *destination,
    SDL_bool cycle);
```

## Function Parameters

|                                                                  |                 |                                                                                           |
| ---------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| [SDL_GpuCopyPass](SDL_GpuCopyPass) *                             | **copyPass**    | a copy pass handle.                                                                       |
| [SDL_GpuTransferBufferLocation](SDL_GpuTransferBufferLocation) * | **source**      | the source transfer buffer with offset.                                                   |
| [SDL_GpuBufferRegion](SDL_GpuBufferRegion) *                     | **destination** | the destination buffer with offset and size.                                              |
| [SDL_bool](SDL_bool)                                             | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the buffer if it is bound, otherwise overwrites the data. |

## Remarks

The upload occurs on the GPU timeline. You may assume that the upload has
finished in subsequent commands.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

