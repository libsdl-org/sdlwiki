###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ReleaseGPUSampler

Frees the given sampler as soon as it is safe to do so.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_ReleaseGPUSampler(
    SDL_GPUDevice *device,
    SDL_GPUSampler *sampler);
```

## Function Parameters

|                                    |             |                            |
| ---------------------------------- | ----------- | -------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *   | **device**  | a GPU context.             |
| [SDL_GPUSampler](SDL_GPUSampler) * | **sampler** | a sampler to be destroyed. |

## Remarks

You must not reference the sampler after calling this function.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

