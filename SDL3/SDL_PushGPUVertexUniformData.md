###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PushGPUVertexUniformData

Pushes data to a vertex uniform slot on the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGPUVertexUniformData(
    SDL_GPUCommandBuffer *command_buffer,
    Uint32 slot_index,
    const void *data,
    Uint32 length);
```

## Function Parameters

|                                                |                    |                                          |
| ---------------------------------------------- | ------------------ | ---------------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                        |
| [Uint32](Uint32)                               | **slot_index**     | the vertex uniform slot to push data to. |
| const void *                                   | **data**           | client data to write.                    |
| [Uint32](Uint32)                               | **length**         | the length of the data to write.         |

## Remarks

Subsequent draw calls will use this uniform data. For information about accessing uniform data from shader, please refer to [SDL_CreateGPUShader](SDL_CreateGPUShader#remarks) remarks section.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

