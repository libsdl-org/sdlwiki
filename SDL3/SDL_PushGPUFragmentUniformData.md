###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PushGPUFragmentUniformData

Pushes data to a fragment uniform slot on the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGPUFragmentUniformData(
    SDL_GPUCommandBuffer *command_buffer,
    Uint32 slot_index,
    const void *data,
    Uint32 length);
```

## Function Parameters

|                                                |                    |                                            |
| ---------------------------------------------- | ------------------ | ------------------------------------------ |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                          |
| Uint32                                         | **slot_index**     | the fragment uniform slot to push data to. |
| const void *                                   | **data**           | client data to write.                      |
| Uint32                                         | **length**         | the length of the data to write.           |

## Remarks

Subsequent draw calls will use this uniform data.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

