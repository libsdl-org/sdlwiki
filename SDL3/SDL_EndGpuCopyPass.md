###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EndGpuCopyPass

Ends the current copy pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_EndGpuCopyPass(
    SDL_GpuCopyPass *copyPass);
```

## Function Parameters

|                                      |              |                     |
| ------------------------------------ | ------------ | ------------------- |
| [SDL_GpuCopyPass](SDL_GpuCopyPass) * | **copyPass** | a copy pass handle. |

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

