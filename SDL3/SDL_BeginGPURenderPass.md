###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BeginGPURenderPass

Begins a render pass on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPURenderPass* SDL_BeginGPURenderPass(
    SDL_GPUCommandBuffer *commandBuffer,
    const SDL_GPUColorAttachmentInfo *colorAttachmentInfos,
    Uint32 colorAttachmentCount,
    const SDL_GPUDepthStencilAttachmentInfo *depthStencilAttachmentInfo);
```

## Function Parameters

|                                                                                |                                |                                                                                       |
| ------------------------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) *                                 | **commandBuffer**              | a command buffer.                                                                     |
| const [SDL_GPUColorAttachmentInfo](SDL_GPUColorAttachmentInfo) *               | **colorAttachmentInfos**       | an array of texture subresources with corresponding clear values and load/store ops.  |
| Uint32                                                                         | **colorAttachmentCount**       | the number of color attachments in the colorAttachmentInfos array.                    |
| const [SDL_GPUDepthStencilAttachmentInfo](SDL_GPUDepthStencilAttachmentInfo) * | **depthStencilAttachmentInfo** | a texture subresource with corresponding clear value and load/store ops, may be NULL. |

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

