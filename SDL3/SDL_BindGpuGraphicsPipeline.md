###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindGpuGraphicsPipeline

Binds a graphics pipeline on a render pass to be used in rendering.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGpuGraphicsPipeline(
    SDL_GpuRenderPass *renderPass,
    SDL_GpuGraphicsPipeline *graphicsPipeline);
```

## Function Parameters

|                                                      |                      |                                |
| ---------------------------------------------------- | -------------------- | ------------------------------ |
| [SDL_GpuRenderPass](SDL_GpuRenderPass) *             | **renderPass**       | a render pass handle.          |
| [SDL_GpuGraphicsPipeline](SDL_GpuGraphicsPipeline) * | **graphicsPipeline** | the graphics pipeline to bind. |

## Remarks

A graphics pipeline must be bound before making any draw calls.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

