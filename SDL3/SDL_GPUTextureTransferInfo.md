###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUTextureTransferInfo

A structure specifying parameters related to transferring data to or from a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUTextureTransferInfo
{
    SDL_GPUTransferBuffer *transfer_buffer;  /**< The transfer buffer used in the transfer operation. */
    Uint32 offset;                           /**< The starting byte of the image data in the transfer buffer. */
    Uint32 pixels_per_row;                   /**< The number of pixels from one row to the next. */
    Uint32 rows_per_layer;                   /**< The number of rows from one layer/depth-slice to the next. */
} SDL_GPUTextureTransferInfo;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

