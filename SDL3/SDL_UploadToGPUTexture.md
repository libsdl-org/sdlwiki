###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

