###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetGPUStencilReference

Sets the current stencil reference value on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGPUStencilReference(
    SDL_GPURenderPass *render_pass,
    Uint8 reference);
```

## Function Parameters

|                                          |                 |                                     |
| ---------------------------------------- | --------------- | ----------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass** | a render pass handle.               |
| Uint8                                    | **reference**   | the stencil reference value to set. |

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

