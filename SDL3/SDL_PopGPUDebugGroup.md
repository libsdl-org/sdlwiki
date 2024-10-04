###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PopGPUDebugGroup

Ends the most-recently pushed debug group.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PopGPUDebugGroup(
    SDL_GPUCommandBuffer *command_buffer);
```

## Function Parameters

|                                                |                    |                   |
| ---------------------------------------------- | ------------------ | ----------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer. |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PushGPUDebugGroup](SDL_PushGPUDebugGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

