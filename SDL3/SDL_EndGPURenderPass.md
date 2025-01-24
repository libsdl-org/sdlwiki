# SDL_EndGPURenderPass

Ends the given render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_EndGPURenderPass(
    SDL_GPURenderPass *render_pass);
```

## Function Parameters

|                                          |                 |                       |
| ---------------------------------------- | --------------- | --------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass** | a render pass handle. |

## Remarks

All bound graphics state on the render pass command buffer is unset. The
render pass handle is now invalid.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

