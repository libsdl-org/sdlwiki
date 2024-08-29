###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGpuBufferName

Sets an arbitrary string constant to label a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGpuBufferName(
    SDL_GpuDevice *device,
    SDL_GpuBuffer *buffer,
    const char *text);
```

## Function Parameters

|                                  |            |                                                            |
| -------------------------------- | ---------- | ---------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU Context.                                             |
| [SDL_GpuBuffer](SDL_GpuBuffer) * | **buffer** | a buffer to attach the name to.                            |
| const char *                     | **text**   | a UTF-8 string constant to mark as the name of the buffer. |

## Remarks

Useful for debugging.

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

