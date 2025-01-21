###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BlitGPUTexture

Blits from a source texture region to a destination texture region.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BlitGPUTexture(
    SDL_GPUCommandBuffer *command_buffer,
    const SDL_GPUBlitInfo *info);
```

## Function Parameters

|                                                |                    |                                                      |
| ---------------------------------------------- | ------------------ | ---------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                                    |
| const [SDL_GPUBlitInfo](SDL_GPUBlitInfo) *     | **info**           | the blit info struct containing the blit parameters. |

## Remarks

This function must not be called inside of any pass.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

