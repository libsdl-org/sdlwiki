# SDL_DownloadFromGPUTexture

Copies data from a texture to a transfer buffer on the GPU timeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DownloadFromGPUTexture(
    SDL_GPUCopyPass *copy_pass,
    const SDL_GPUTextureRegion *source,
    const SDL_GPUTextureTransferInfo *destination);
```

## Function Parameters

|                                                                  |                 |                                                                |
| ---------------------------------------------------------------- | --------------- | -------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                             | **copy_pass**   | a copy pass handle.                                            |
| const [SDL_GPUTextureRegion](SDL_GPUTextureRegion) *             | **source**      | the source texture region.                                     |
| const [SDL_GPUTextureTransferInfo](SDL_GPUTextureTransferInfo) * | **destination** | the destination transfer buffer with image layout information. |

## Remarks

This data is not guaranteed to be copied until the command buffer fence is
signaled.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

