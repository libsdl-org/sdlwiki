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

**WARNING**: On some older/integrated hardware, Direct3D 12 requires
texture data row pitch to be 256 byte aligned, and offsets to be aligned to
512 bytes. If they are not, SDL will make a temporary copy of the data that
is properly aligned, but this adds overhead to the transfer process. Apps
can avoid this by aligning their data appropriately, or using a different
GPU backend than Direct3D 12.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

