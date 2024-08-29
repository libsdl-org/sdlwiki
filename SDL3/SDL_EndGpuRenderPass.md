###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EndGpuRenderPass

Ends the given render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_EndGpuRenderPass(
    SDL_GpuRenderPass *renderPass);
```

## Function Parameters

|                                          |                |                       |
| ---------------------------------------- | -------------- | --------------------- |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) * | **renderPass** | a render pass handle. |

## Remarks

All bound graphics state on the render pass command buffer is unset. The
render pass handle is now invalid.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

