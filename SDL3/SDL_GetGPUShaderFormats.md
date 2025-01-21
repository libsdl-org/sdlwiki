###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGPUShaderFormats

Returns the supported shader formats for this GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUShaderFormat SDL_GetGPUShaderFormats(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                         |
| -------------------------------- | ---------- | ----------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context to query. |

## Return Value

([SDL_GPUShaderFormat](SDL_GPUShaderFormat)) Returns a bitflag indicating
which shader formats the driver is able to consume.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

