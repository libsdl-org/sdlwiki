###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUDevice

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUDevice* SDL_CreateGPUDevice(
    SDL_GPUShaderFormat formatFlags,
    SDL_bool debugMode,
    const char *name);
```

## Function Parameters

|                                            |                 |                                                                       |
| ------------------------------------------ | --------------- | --------------------------------------------------------------------- |
| [SDL_GPUShaderFormat](SDL_GPUShaderFormat) | **formatFlags** | a bitflag indicating which shader formats the app is able to provide. |
| [SDL_bool](SDL_bool)                       | **debugMode**   | enable debug mode properties and validations.                         |
| const char *                               | **name**        | the preferred GPU driver, or NULL to let SDL pick the optimal driver. |

## Return Value

([SDL_GPUDevice](SDL_GPUDevice) *) Returns a GPU context on success or NULL
on failure.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGPUDriver](SDL_GetGPUDriver)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

