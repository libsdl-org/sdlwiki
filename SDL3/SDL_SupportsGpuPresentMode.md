###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SupportsGpuPresentMode

Determines whether a presentation mode is supported by the window.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_SupportsGpuPresentMode(
    SDL_GpuDevice *device,
    SDL_Window *window,
    SDL_GpuPresentMode presentMode);
```

## Function Parameters

|                                          |                 |                                 |
| ---------------------------------------- | --------------- | ------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *         | **device**      | a GPU context.                  |
| [SDL_Window](SDL_Window) *               | **window**      | an [SDL_Window](SDL_Window).    |
| [SDL_GpuPresentMode](SDL_GpuPresentMode) | **presentMode** | the presentation mode to check. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if supported,
[SDL_FALSE](SDL_FALSE) if unsupported (or on error).

## Remarks

The window must be claimed before calling this function.

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_ClaimGpuWindow](SDL_ClaimGpuWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

