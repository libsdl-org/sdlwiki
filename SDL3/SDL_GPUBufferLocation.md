###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUBufferLocation

A structure specifying a location in a buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUBufferLocation
{
    SDL_GPUBuffer *buffer;  /**< The buffer. */
    Uint32 offset;          /**< The starting byte within the buffer. */
} SDL_GPUBufferLocation;
```

## Remarks

Used when copying data between buffers.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_CopyGPUBufferToBuffer](SDL_CopyGPUBufferToBuffer)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

