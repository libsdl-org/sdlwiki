# SDL_GPUCopyPass

An opaque handle representing a copy pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUCopyPass SDL_GPUCopyPass;
```

## Remarks

This handle is transient and should not be held or referenced after
[SDL_EndGPUCopyPass](SDL_EndGPUCopyPass) is called.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_BeginGPUCopyPass](SDL_BeginGPUCopyPass)
- [SDL_EndGPUCopyPass](SDL_EndGPUCopyPass)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

