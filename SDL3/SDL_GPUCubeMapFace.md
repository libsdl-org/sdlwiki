###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUCubeMapFace

Specifies the face of a cube map.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUCubeMapFace
{
    SDL_GPU_CUBEMAPFACE_POSITIVEX,
    SDL_GPU_CUBEMAPFACE_NEGATIVEX,
    SDL_GPU_CUBEMAPFACE_POSITIVEY,
    SDL_GPU_CUBEMAPFACE_NEGATIVEY,
    SDL_GPU_CUBEMAPFACE_POSITIVEZ,
    SDL_GPU_CUBEMAPFACE_NEGATIVEZ
} SDL_GPUCubeMapFace;
```

## Remarks

Can be passed in as the layer field in texture-related structs.

## Version

This enum is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

