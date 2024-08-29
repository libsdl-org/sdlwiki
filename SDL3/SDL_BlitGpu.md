###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitGpu

Blits from a source texture region to a destination texture region.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BlitGpu(
    SDL_GpuCommandBuffer *commandBuffer,
    SDL_GpuBlitRegion *source,
    SDL_GpuBlitRegion *destination,
    SDL_FlipMode flipMode,
    SDL_GpuFilter filterMode,
    SDL_bool cycle);
```

## Function Parameters

|                                                |                   |                                                                                                                             |
| ---------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer.                                                                                                           |
| [SDL_GpuBlitRegion](SDL_GpuBlitRegion) *       | **source**        | the texture region to copy from.                                                                                            |
| [SDL_GpuBlitRegion](SDL_GpuBlitRegion) *       | **destination**   | the texture region to copy to.                                                                                              |
| [SDL_FlipMode](SDL_FlipMode)                   | **flipMode**      | the flip mode for the source texture region.                                                                                |
| [SDL_GpuFilter](SDL_GpuFilter)                 | **filterMode**    | the filter mode that will be used when blitting.                                                                            |
| [SDL_bool](SDL_bool)                           | **cycle**         | if [SDL_TRUE](SDL_TRUE), cycles the destination texture if the destination texture is bound, otherwise overwrites the data. |

## Remarks

This function must not be called inside of any pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


