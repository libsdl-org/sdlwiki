###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGPUDeviceDriver

Returns the name of the backend used to create this GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
const char * SDL_GetGPUDeviceDriver(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                         |
| -------------------------------- | ---------- | ----------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context to query. |

## Return Value

(const char *) Returns the name of the device's driver, or NULL on error.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

