###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CopyGPUBufferToBuffer

Performs a buffer-to-buffer copy.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_CopyGPUBufferToBuffer(
    SDL_GPUCopyPass *copyPass,
    const SDL_GPUBufferLocation *source,
    const SDL_GPUBufferLocation *destination,
    Uint32 size,
    SDL_bool cycle);
```

## Function Parameters

|                                                        |                 |                                                                                                       |
| ------------------------------------------------------ | --------------- | ----------------------------------------------------------------------------------------------------- |
| [SDL_GPUCopyPass](SDL_GPUCopyPass) *                   | **copyPass**    | a copy pass handle.                                                                                   |
| const [SDL_GPUBufferLocation](SDL_GPUBufferLocation) * | **source**      | the buffer and offset to copy from.                                                                   |
| const [SDL_GPUBufferLocation](SDL_GPUBufferLocation) * | **destination** | the buffer and offset to copy to.                                                                     |
| Uint32                                                 | **size**        | the length of the buffer to copy.                                                                     |
| [SDL_bool](SDL_bool)                                   | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the destination buffer if it is bound, otherwise overwrites the data. |

## Remarks

This copy occurs on the GPU timeline. You may assume the copy has finished
in subsequent commands.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

