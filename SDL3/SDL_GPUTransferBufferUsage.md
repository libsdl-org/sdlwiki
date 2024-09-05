###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUTransferBufferUsage

Specifies how a transfer buffer is intended to be used by the client.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUTransferBufferUsage
{
    SDL_GPU_TRANSFERBUFFERUSAGE_UPLOAD,
    SDL_GPU_TRANSFERBUFFERUSAGE_DOWNLOAD
} SDL_GPUTransferBufferUsage;
```

## Remarks

Note that mapping and copying FROM an upload transfer buffer or TO a
download transfer buffer is undefined behavior.

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_CreateGPUTransferBuffer](SDL_CreateGPUTransferBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

