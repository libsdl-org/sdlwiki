###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_UploadToGPUBuffer

Uploads data from a transfer buffer to a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UploadToGPUBuffer(
    SDL_GPUCopyPass *copy_pass,
    const SDL_GPUTransferBufferLocation *source,
    const SDL_GPUBufferRegion *destination,
    bool cycle);
```

## Function Parameters

|                                                                        |                 |                                                                                   |
| ---------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                                   | **copy_pass**   | a copy pass handle.                                                               |
| const [SDL_GPUTransferBufferLocation](SDL_GPUTransferBufferLocation) * | **source**      | the source transfer buffer with offset.                                           |
| const [SDL_GPUBufferRegion](SDL_GPUBufferRegion) *                     | **destination** | the destination buffer with offset and size.                                      |
| bool                                                                   | **cycle**       | if true, cycles the buffer if it is already bound, otherwise overwrites the data. |

## Remarks

The upload occurs on the GPU timeline. You may assume that the upload has
finished in subsequent commands.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

