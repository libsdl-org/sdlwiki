###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DownloadFromGPUTexture

Copies data from a texture to a transfer buffer on the GPU timeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DownloadFromGPUTexture(
    SDL_GPUCopyPass *copyPass,
    SDL_GPUTextureRegion *source,
    SDL_GPUTextureTransferInfo *destination);
```

## Function Parameters

|                                                            |                 |                                                                |
| ---------------------------------------------------------- | --------------- | -------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                       | **copyPass**    | a copy pass handle.                                            |
| [SDL_GPUTextureRegion](SDL_GPUTextureRegion) *             | **source**      | the source texture region.                                     |
| [SDL_GPUTextureTransferInfo](SDL_GPUTextureTransferInfo) * | **destination** | the destination transfer buffer with image layout information. |

## Remarks

This data is not guaranteed to be copied until the command buffer fence is
signaled.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

