###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetGPUBlendConstants

Sets the current blend constants on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGPUBlendConstants(
    SDL_GPURenderPass *render_pass,
    SDL_FColor blend_constants);
```

## Function Parameters

|                                          |                     |                           |
| ---------------------------------------- | ------------------- | ------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass**     | a render pass handle.     |
| [SDL_FColor](SDL_FColor)                 | **blend_constants** | the blend constant color. |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GPU_BLENDFACTOR_CONSTANT_COLOR](SDL_GPU_BLENDFACTOR_CONSTANT_COLOR)
- [SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR](SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

