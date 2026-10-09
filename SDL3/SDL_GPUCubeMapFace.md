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

Can be passed in as the layer index in texture-related structs.

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_GPUTextureLocation](SDL_GPUTextureLocation)
- [SDL_GPUTextureRegion](SDL_GPUTextureRegion)
- [SDL_GPUBlitRegion](SDL_GPUBlitRegion)
- [SDL_GPUColorTargetInfo](SDL_GPUColorTargetInfo)
- [SDL_GPUDepthStencilTargetInfo](SDL_GPUDepthStencilTargetInfo)
- [SDL_GPUStorageTextureReadWriteBinding](SDL_GPUStorageTextureReadWriteBinding)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

