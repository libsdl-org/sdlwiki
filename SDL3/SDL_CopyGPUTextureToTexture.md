# SDL_CopyGPUTextureToTexture

Performs a texture-to-texture copy.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_CopyGPUTextureToTexture(
    SDL_GPUCopyPass *copy_pass,
    const SDL_GPUTextureLocation *source,
    const SDL_GPUTextureLocation *destination,
    Uint32 w,
    Uint32 h,
    Uint32 d,
    bool cycle);
```

## Function Parameters

|                                                          |                 |                                                                                                             |
| -------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                     | **copy_pass**   | a copy pass handle.                                                                                         |
| const [SDL_GPUTextureLocation](SDL_GPUTextureLocation) * | **source**      | a source texture region.                                                                                    |
| const [SDL_GPUTextureLocation](SDL_GPUTextureLocation) * | **destination** | a destination texture region.                                                                               |
| [Uint32](Uint32)                                         | **w**           | the width of the region to copy.                                                                            |
| [Uint32](Uint32)                                         | **h**           | the height of the region to copy.                                                                           |
| [Uint32](Uint32)                                         | **d**           | the depth of the region to copy.                                                                            |
| bool                                                     | **cycle**       | if true, cycles the destination texture if the destination texture is bound, otherwise overwrites the data. |

## Remarks

This copy occurs on the GPU timeline. You may assume the copy has finished
in subsequent commands.

This function does not support copying between depth and color textures.
For those, copy the texture to a buffer and then to the destination
texture.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

