###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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
    SDL_bool cycle);
```

## Function Parameters

|                                                                        |                 |                                                                                           |
| ---------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                                   | **copy_pass**   | a copy pass handle.                                                                       |
| const [SDL_GPUTransferBufferLocation](SDL_GPUTransferBufferLocation) * | **source**      | the source transfer buffer with offset.                                                   |
| const [SDL_GPUBufferRegion](SDL_GPUBufferRegion) *                     | **destination** | the destination buffer with offset and size.                                              |
| [SDL_bool](SDL_bool)                                                   | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the buffer if it is bound, otherwise overwrites the data. |

## Remarks

The upload occurs on the GPU timeline. You may assume that the upload has
finished in subsequent commands.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

