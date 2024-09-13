###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_QueryGPUSupport

Checks for GPU runtime support.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_QueryGPUSupport(
    SDL_GPUShaderFormat format_flags,
    const char *name);
```

## Function Parameters

|                                            |                  |                                                                       |
| ------------------------------------------ | ---------------- | --------------------------------------------------------------------- |
| [SDL_GPUShaderFormat](SDL_GPUShaderFormat) | **format_flags** | a bitflag indicating which shader formats the app is able to provide. |
| const char *                               | **name**         | the preferred GPU driver, or NULL to let SDL pick the optimal driver. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if supported,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateGPUDevice](SDL_CreateGPUDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

