###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitGPU

Blits from a source texture region to a destination texture region.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BlitGPU(
    SDL_GPUCommandBuffer *commandBuffer,
    SDL_GPUBlitRegion *source,
    SDL_GPUBlitRegion *destination,
    SDL_FlipMode flipMode,
    SDL_GPUFilter filterMode,
    bool cycle);
```

## Function Parameters

|                                                |                   |                                                                                                                             |
| ---------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **commandBuffer** | a command buffer.                                                                                                           |
| [SDL_GPUBlitRegion](SDL_GPUBlitRegion) *       | **source**        | the texture region to copy from.                                                                                            |
| [SDL_GPUBlitRegion](SDL_GPUBlitRegion) *       | **destination**   | the texture region to copy to.                                                                                              |
| [SDL_FlipMode](SDL_FlipMode)                   | **flipMode**      | the flip mode for the source texture region.                                                                                |
| [SDL_GPUFilter](SDL_GPUFilter)                 | **filterMode**    | the filter mode that will be used when blitting.                                                                            |
| [bool](bool)                           | **cycle**         | if [true](true), cycles the destination texture if the destination texture is bound, otherwise overwrites the data. |

## Remarks

This function must not be called inside of any pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

