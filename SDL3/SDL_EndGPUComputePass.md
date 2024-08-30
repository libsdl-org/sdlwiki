###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EndGPUComputePass

Ends the current compute pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_EndGPUComputePass(
    SDL_GPUComputePass *computePass);
```

## Function Parameters

|                                            |                 |                        |
| ------------------------------------------ | --------------- | ---------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) * | **computePass** | a compute pass handle. |

## Remarks

All bound compute state on the command buffer is unset. The compute pass
handle is now invalid.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

