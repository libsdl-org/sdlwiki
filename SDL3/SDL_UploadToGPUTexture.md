# SDL_UploadToGPUTexture

Uploads data from a transfer buffer to a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UploadToGPUTexture(
    SDL_GPUCopyPass *copy_pass,
    const SDL_GPUTextureTransferInfo *source,
    const SDL_GPUTextureRegion *destination,
    bool cycle);
```

## Function Parameters

|                                                                  |                 |                                                                                     |
| ---------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                             | **copy_pass**   | a copy pass handle.                                                                 |
| const [SDL_GPUTextureTransferInfo](SDL_GPUTextureTransferInfo) * | **source**      | the source transfer buffer with image layout information.                           |
| const [SDL_GPUTextureRegion](SDL_GPUTextureRegion) *             | **destination** | the destination texture region.                                                     |
| bool                                                             | **cycle**       | if true, cycles the texture if the texture is bound, otherwise overwrites the data. |

## Remarks

The upload occurs on the GPU timeline. You may assume that the upload has
finished in subsequent commands.

You must align the data in the transfer buffer to a multiple of the texel
size of the texture format.

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

