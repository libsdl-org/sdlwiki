###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BeginGPURenderPass

Begins a render pass on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPURenderPass* SDL_BeginGPURenderPass(
    SDL_GPUCommandBuffer *command_buffer,
    const SDL_GPUColorTargetInfo *color_target_infos,
    Uint32 num_color_targets,
    const SDL_GPUDepthStencilTargetInfo *depth_stencil_target_info);
```

## Function Parameters

|                                                                        |                               |                                                                                       |
| ---------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) *                         | **command_buffer**            | a command buffer.                                                                     |
| const [SDL_GPUColorTargetInfo](SDL_GPUColorTargetInfo) *               | **color_target_infos**        | an array of texture subresources with corresponding clear values and load/store ops.  |
| Uint32                                                                 | **num_color_targets**         | the number of color targets in the color_target_infos array.                          |
| const [SDL_GPUDepthStencilTargetInfo](SDL_GPUDepthStencilTargetInfo) * | **depth_stencil_target_info** | a texture subresource with corresponding clear value and load/store ops, may be NULL. |

## Return Value

([SDL_GPURenderPass](SDL_GPURenderPass) *) Returns a render pass handle.

## Remarks

A render pass consists of a set of texture subresources (or depth slices in
the 3D texture case) which will be rendered to during the render pass,
along with corresponding clear values and load/store operations. All
operations related to graphics pipelines must take place inside of a render
pass. A default viewport and scissor state are automatically set when this
is called. You cannot begin another render pass, or begin a compute pass or
copy pass until you have ended the render pass.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_EndGPURenderPass](SDL_EndGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

