###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGPUSwapchainTextureFormat

Obtains the texture format of the swapchain for the given window.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTextureFormat SDL_GetGPUSwapchainTextureFormat(
    SDL_GPUDevice *device,
    SDL_Window *window);
```

## Function Parameters

|                                  |            |                                                    |
| -------------------------------- | ---------- | -------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context.                                     |
| [SDL_Window](SDL_Window) *       | **window** | an [SDL_Window](SDL_Window) that has been claimed. |

## Return Value

([SDL_GPUTextureFormat](SDL_GPUTextureFormat)) Returns the texture format
of the swapchain.

## Remarks

Note that this format can change if the swapchain parameters change.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

