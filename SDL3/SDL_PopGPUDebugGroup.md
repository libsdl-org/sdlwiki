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

## Remarks

On Direct3D 12, using
[SDL_PopGPUDebugGroup](SDL_PopGPUDebugGroup) will cause validation errors
unless you have WinPixEventRuntime.dll in your PATH. See
[here](https://devblogs.microsoft.com/pix/winpixeventruntime/)
for instructions on how to obtain it.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PushGPUDebugGroup](SDL_PushGPUDebugGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

