###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PushGpuVertexUniformData

Pushes data to a vertex uniform slot on the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGpuVertexUniformData(
    SDL_GpuCommandBuffer *commandBuffer,
    Uint32 slotIndex,
    const void *data,
    Uint32 dataLengthInBytes);
```

## Function Parameters

|                                                |                       |                                          |
| ---------------------------------------------- | --------------------- | ---------------------------------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer**     | a command buffer.                        |
| Uint32                                         | **slotIndex**         | the vertex uniform slot to push data to. |
| const void *                                   | **data**              | client data to write.                    |
| Uint32                                         | **dataLengthInBytes** | the length of the data to write.         |

## Remarks

Subsequent draw calls will use this uniform data.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

