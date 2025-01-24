# SDL_SetGPUViewport

Sets the current viewport state on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGPUViewport(
    SDL_GPURenderPass *render_pass,
    const SDL_GPUViewport *viewport);
```

## Function Parameters

|                                            |                 |                       |
| ------------------------------------------ | --------------- | --------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) *   | **render_pass** | a render pass handle. |
| const [SDL_GPUViewport](SDL_GPUViewport) * | **viewport**    | the viewport to set.  |

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

