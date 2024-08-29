###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyGpuDevice

Destroys a GPU context previously returned by [SDL_CreateGpuDevice](SDL_CreateGpuDevice).

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_DestroyGpuDevice(SDL_GpuDevice *device);
```

## Function Parameters

|                                  |            |                           |
| -------------------------------- | ---------- | ------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU Context to destroy. |

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_CreateGpuDevice](SDL_CreateGpuDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

