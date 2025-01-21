###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ReleaseGPUBuffer

Frees the given buffer as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGPUBuffer(
    SDL_GPUDevice *device,
    SDL_GPUBuffer *buffer);
```

## Function Parameters

|                                  |            |                           |
| -------------------------------- | ---------- | ------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context.            |
| [SDL_GPUBuffer](SDL_GPUBuffer) * | **buffer** | a buffer to be destroyed. |

## Remarks

You must not reference the buffer after calling this function.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

