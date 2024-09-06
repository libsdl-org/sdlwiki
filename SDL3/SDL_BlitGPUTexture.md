###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitGPUTexture

Blits from a source texture region to a destination texture region.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BlitGPUTexture(
    SDL_GPUCommandBuffer *command_buffer,
    const SDL_GPUBlitRegion *source,
    const SDL_GPUBlitRegion *destination,
    SDL_FlipMode flip_mode,
    SDL_GPUFilter filter,
    SDL_bool cycle);
```

## Function Parameters

|                                                |                    |                                                                                                                             |
| ---------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                                                                                                           |
| const [SDL_GPUBlitRegion](SDL_GPUBlitRegion) * | **source**         | the texture region to copy from.                                                                                            |
| const [SDL_GPUBlitRegion](SDL_GPUBlitRegion) * | **destination**    | the texture region to copy to.                                                                                              |
| [SDL_FlipMode](SDL_FlipMode)                   | **flip_mode**      | the flip mode for the source texture region.                                                                                |
| [SDL_GPUFilter](SDL_GPUFilter)                 | **filter**         | the filter mode that will be used when blitting.                                                                            |
| [SDL_bool](SDL_bool)                           | **cycle**          | if [SDL_TRUE](SDL_TRUE), cycles the destination texture if the destination texture is bound, otherwise overwrites the data. |

## Remarks

This function must not be called inside of any pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

