###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PopGpuDebugGroup

Ends the most-recently pushed debug group.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PopGpuDebugGroup(
    SDL_GpuCommandBuffer *commandBuffer);
```

## Function Parameters

|                                                |                   |                   |
| ---------------------------------------------- | ----------------- | ----------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer. |

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_PushGpuDebugGroup](SDL_PushGpuDebugGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

