###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CopyGpuBufferToBuffer

Performs a buffer-to-buffer copy.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_CopyGpuBufferToBuffer(
    SDL_GpuCopyPass *copyPass,
    SDL_GpuBufferLocation *source,
    SDL_GpuBufferLocation *destination,
    Uint32 size,
    SDL_bool cycle);
```

## Function Parameters

|                                                  |                 |                                                                                                       |
| ------------------------------------------------ | --------------- | ----------------------------------------------------------------------------------------------------- |
| [SDL_GpuCopyPass](SDL_GpuCopyPass) *             | **copyPass**    | a copy pass handle.                                                                                   |
| [SDL_GpuBufferLocation](SDL_GpuBufferLocation) * | **source**      | the buffer and offset to copy from.                                                                   |
| [SDL_GpuBufferLocation](SDL_GpuBufferLocation) * | **destination** | the buffer and offset to copy to.                                                                     |
| Uint32                                           | **size**        | the length of the buffer to copy.                                                                     |
| [SDL_bool](SDL_bool)                             | **cycle**       | if [SDL_TRUE](SDL_TRUE), cycles the destination buffer if it is bound, otherwise overwrites the data. |

## Remarks

This copy occurs on the GPU timeline. You may assume the copy has finished
in subsequent commands.

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

