###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUSupportsShaderFormats

Checks for GPU runtime support.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
bool SDL_GPUSupportsShaderFormats(
    SDL_GPUShaderFormat format_flags,
    const char *name);
```

## Function Parameters

|                                            |                  |                                                                       |
| ------------------------------------------ | ---------------- | --------------------------------------------------------------------- |
| [SDL_GPUShaderFormat](SDL_GPUShaderFormat) | **format_flags** | a bitflag indicating which shader formats the app is able to provide. |
| const char *                               | **name**         | the preferred GPU driver, or NULL to let SDL pick the optimal driver. |

## Return Value

(bool) Returns true if supported, false otherwise.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUDevice](SDL_CreateGPUDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

