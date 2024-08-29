###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PushGpuDebugGroup

Begins a debug group with an arbitary name.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGpuDebugGroup(
    SDL_GpuCommandBuffer *commandBuffer,
    const char *name);
```

## Function Parameters

|                                                |                   |                                               |
| ---------------------------------------------- | ----------------- | --------------------------------------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer.                             |
| const char *                                   | **name**          | a UTF-8 string constant that names the group. |

## Remarks

Used for denoting groups of calls when viewing the command buffer
callstream in a graphics debugging tool.

Each call to [SDL_PushGpuDebugGroup](SDL_PushGpuDebugGroup) must have a
corresponding call to [SDL_PopGpuDebugGroup](SDL_PopGpuDebugGroup).

On some backends (e.g. Metal), pushing a debug group during a
render/blit/compute pass will create a group that is scoped to the native
pass rather than the command buffer. For best results, if you push a debug
group during a pass, always pop it in the same pass.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PopGpuDebugGroup](SDL_PopGpuDebugGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

