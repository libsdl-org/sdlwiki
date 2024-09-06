###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGPUScissor

Sets the current scissor state on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGPUScissor(
    SDL_GPURenderPass *render_pass,
    const SDL_Rect *scissor);
```

## Function Parameters

|                                          |                 |                          |
| ---------------------------------------- | --------------- | ------------------------ |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass** | a render pass handle.    |
| const [SDL_Rect](SDL_Rect) *             | **scissor**     | the scissor area to set. |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

