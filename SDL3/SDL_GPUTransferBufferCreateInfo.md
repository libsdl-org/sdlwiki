# SDL_GPUTransferBufferCreateInfo

A structure specifying the parameters of a transfer buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUTransferBufferCreateInfo
{
    SDL_GPUTransferBufferUsage usage;  /**< How the transfer buffer is intended to be used by the client. */
    Uint32 size;                       /**< The size in bytes of the transfer buffer. */

    SDL_PropertiesID props;            /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
} SDL_GPUTransferBufferCreateInfo;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUTransferBuffer](SDL_CreateGPUTransferBuffer)






----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

