###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CopyGPUTextureToTexture

Performs a texture-to-texture copy.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_CopyGPUTextureToTexture(
    SDL_GPUCopyPass *copyPass,
    SDL_GPUTextureLocation *source,
    SDL_GPUTextureLocation *destination,
    Uint32 w,
    Uint32 h,
    Uint32 d,
    SDL_bool cycle);
```

## Function Parameters

|                                                    |                 |                                                                                                                             |
| -------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *               | **copyPass**    | a copy pass handle.                                                                                                         |
| [SDL_GPUTextureLocation](SDL_GPUTextureLocation) * | **source**      | a source texture region.                                                                                                    |
| [SDL_GPUTextureLocation](SDL_GPUTextureLocation) * | **destination** | a destination texture region.                                                                                               |
| Uint32                                             | **w**           | the width of the region to copy.                                                                                            |
| Uint32                                             | **h**           | the height of the region to copy.                                                                                           |
| Uint32                                             | **d**           | the depth of the region to copy.                                                                                            |
| [SDL_bool](SDL_bool)                               | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the destination texture if the destination texture is bound, otherwise overwrites the data. |

## Remarks

This copy occurs on the GPU timeline. You may assume the copy has finished
in subsequent commands.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

