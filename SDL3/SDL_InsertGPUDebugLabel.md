# SDL_InsertGPUDebugLabel

Inserts an arbitrary string label into the command buffer callstream.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_InsertGPUDebugLabel(
    SDL_GPUCommandBuffer *command_buffer,
    const char *text);
```

## Function Parameters

|                                                |                    |                                                 |
| ---------------------------------------------- | ------------------ | ----------------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                               |
| const char *                                   | **text**           | a UTF-8 string constant to insert as the label. |

## Remarks

Useful for debugging.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

