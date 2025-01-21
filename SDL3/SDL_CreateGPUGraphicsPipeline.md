###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateGPUGraphicsPipeline

Creates a pipeline object to be used in a graphics workflow.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUGraphicsPipeline* SDL_CreateGPUGraphicsPipeline(
    SDL_GPUDevice *device,
    const SDL_GPUGraphicsPipelineCreateInfo *createinfo);
```

## Function Parameters

|                                                                                |                |                                                                   |
| ------------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                                               | **device**     | a GPU Context.                                                    |
| const [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo) * | **createinfo** | a struct describing the state of the graphics pipeline to create. |

## Return Value

([SDL_GPUGraphicsPipeline](SDL_GPUGraphicsPipeline) *) Returns a graphics
pipeline object on success, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

There are optional properties that can be provided through `props`. These
are the supported properties:

- [`SDL_PROP_GPU_GRAPHICSPIPELINE_CREATE_NAME_STRING`](SDL_PROP_GPU_GRAPHICSPIPELINE_CREATE_NAME_STRING):
  a name that can be displayed in debugging tools.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUShader](SDL_CreateGPUShader)
- [SDL_BindGPUGraphicsPipeline](SDL_BindGPUGraphicsPipeline)
- [SDL_ReleaseGPUGraphicsPipeline](SDL_ReleaseGPUGraphicsPipeline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

