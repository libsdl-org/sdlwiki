###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnclaimGpuWindow

Unclaims a window, destroying its swapchain structure.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_UnclaimGpuWindow(
    SDL_GpuDevice *device,
    SDL_Window *window);
```

## Function Parameters

|                                  |            |                                                    |
| -------------------------------- | ---------- | -------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context.                                     |
| [SDL_Window](SDL_Window) *       | **window** | an [SDL_Window](SDL_Window) that has been claimed. |

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_ClaimGpuWindow](SDL_ClaimGpuWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

