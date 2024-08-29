###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DownloadFromGpuTexture

Copies data from a texture to a transfer buffer on the GPU timeline.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DownloadFromGpuTexture(
    SDL_GpuCopyPass *copyPass,
    SDL_GpuTextureRegion *source,
    SDL_GpuTextureTransferInfo *destination);
```

## Function Parameters

|                                                            |                 |                                                                |
| ---------------------------------------------------------- | --------------- | -------------------------------------------------------------- |
| [SDL_GpuCopyPass](SDL_GpuCopyPass) *                       | **copyPass**    | a copy pass handle.                                            |
| [SDL_GpuTextureRegion](SDL_GpuTextureRegion) *             | **source**      | the source texture region.                                     |
| [SDL_GpuTextureTransferInfo](SDL_GpuTextureTransferInfo) * | **destination** | the destination transfer buffer with image layout information. |

## Remarks

This data is not guaranteed to be copied until the command buffer fence is
signaled.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

