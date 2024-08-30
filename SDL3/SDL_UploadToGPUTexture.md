###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UploadToGPUTexture

Uploads data from a transfer buffer to a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UploadToGPUTexture(
    SDL_GPUCopyPass *copyPass,
    SDL_GPUTextureTransferInfo *source,
    SDL_GPUTextureRegion *destination,
    SDL_bool cycle);
```

## Function Parameters

|                                                            |                 |                                                                                                     |
| ---------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                       | **copyPass**    | a copy pass handle.                                                                                 |
| [SDL_GPUTextureTransferInfo](SDL_GPUTextureTransferInfo) * | **source**      | the source transfer buffer with image layout information.                                           |
| [SDL_GPUTextureRegion](SDL_GPUTextureRegion) *             | **destination** | the destination texture region.                                                                     |
| [SDL_bool](SDL_bool)                                       | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the texture if the texture is bound, otherwise overwrites the data. |

## Remarks

The upload occurs on the GPU timeline. You may assume that the upload has
finished in subsequent commands.

You must align the data in the transfer buffer to a multiple of the texel
size of the texture format.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

