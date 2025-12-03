# SDL_PushGPUDebugGroup

Begins a debug group with an arbitrary name.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGPUDebugGroup(
    SDL_GPUCommandBuffer *command_buffer,
    const char *name);
```

## Function Parameters

|                                                |                    |                                               |
| ---------------------------------------------- | ------------------ | --------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                             |
| const char *                                   | **name**           | a UTF-8 string constant that names the group. |

## Remarks

Used for denoting groups of calls when viewing the command buffer
callstream in a graphics debugging tool.

Each call to [SDL_PushGPUDebugGroup](SDL_PushGPUDebugGroup) must have a
corresponding call to [SDL_PopGPUDebugGroup](SDL_PopGPUDebugGroup).

On Direct3D 12, using
[SDL_PushGPUDebugGroup](SDL_PushGPUDebugGroup) will cause validation errors
unless you have WinPixEventRuntime.dll in your PATH. See
[here](https://devblogs.microsoft.com/pix/winpixeventruntime/)
for instructions on how to obtain it.

On some backends (e.g. Metal), pushing a debug group during a
render/blit/compute pass will create a group that is scoped to the native
pass rather than the command buffer. For best results, if you push a debug
group during a pass, always pop it in the same pass.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PopGPUDebugGroup](SDL_PopGPUDebugGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

