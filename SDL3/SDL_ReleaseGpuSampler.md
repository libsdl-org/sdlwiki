###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseGpuSampler

Frees the given sampler as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGpuSampler(
    SDL_GpuDevice *device,
    SDL_GpuSampler *sampler);
```

## Function Parameters

|                                    |             |                            |
| ---------------------------------- | ----------- | -------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *   | **device**  | a GPU context.             |
| [SDL_GpuSampler](SDL_GpuSampler) * | **sampler** | a sampler to be destroyed. |

## Remarks

You must not reference the texture after calling this function.

## Version

This function is available since SDL 3.x.x

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

