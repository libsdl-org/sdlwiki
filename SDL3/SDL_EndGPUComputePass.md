# SDL_EndGPUComputePass

Ends the current compute pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_EndGPUComputePass(
    SDL_GPUComputePass *compute_pass);
```

## Function Parameters

|                                            |                  |                        |
| ------------------------------------------ | ---------------- | ---------------------- |
| [SDL_GPUComputePass](SDL_GPUComputePass) * | **compute_pass** | a compute pass handle. |

## Remarks

All bound compute state on the command buffer is unset. The compute pass
handle is now invalid.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

