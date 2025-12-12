# SDL_PushGPUComputeUniformData

Pushes data to a uniform slot on the command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_PushGPUComputeUniformData(
    SDL_GPUCommandBuffer *command_buffer,
    Uint32 slot_index,
    const void *data,
    Uint32 length);
```

## Function Parameters

|                                                |                    |                                   |
| ---------------------------------------------- | ------------------ | --------------------------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer.                 |
| [Uint32](Uint32)                               | **slot_index**     | the uniform slot to push data to. |
| const void *                                   | **data**           | client data to write.             |
| [Uint32](Uint32)                               | **length**         | the length of the data to write.  |

## Remarks

Subsequent draw calls in the same command buffer will reuse this uniform data.

The data being pushed must respect std140 layout conventions. In practical
terms this means you must ensure that vec3 and vec4 fields are 16-byte
aligned.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

