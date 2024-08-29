###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuGraphicsPipeline

Creates a pipeline object to be used in a graphics workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuGraphicsPipeline* SDL_CreateGpuGraphicsPipeline(
    SDL_GpuDevice *device,
    SDL_GpuGraphicsPipelineCreateInfo *pipelineCreateInfo);
```

## Function Parameters

|                                                                          |                        |                                                                 |
| ------------------------------------------------------------------------ | ---------------------- | --------------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                                         | **device**             | a GPU Context.                                                  |
| [SDL_GpuGraphicsPipelineCreateInfo](SDL_GpuGraphicsPipelineCreateInfo) * | **pipelineCreateInfo** | a struct describing the state of the desired graphics pipeline. |

## Return Value

([SDL_GpuGraphicsPipeline](SDL_GpuGraphicsPipeline) *) Returns a graphics
pipeline object on success, or NULL on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateGpuShader](SDL_CreateGpuShader)
- [SDL_BindGpuGraphicsPipeline](SDL_BindGpuGraphicsPipeline)
- [SDL_ReleaseGpuGraphicsPipeline](SDL_ReleaseGpuGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

