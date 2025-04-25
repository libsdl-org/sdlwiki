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

## Remarks

If either of `pixels_per_row` or `rows_per_layer` is zero, then width and
height of passed [SDL_GPUTextureRegion](SDL_GPUTextureRegion) to
[SDL_UploadToGPUTexture](SDL_UploadToGPUTexture) or
[SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture) are used as
default values respectively and data is considered to be tightly packed.

**WARNING**: Direct3D 12 requires texture data row pitch to be 256 byte
aligned, and offsets to be aligned to 512 bytes. If they are not, SDL will
make a temporary copy of the data that is properly aligned, but this adds
overhead to the transfer process. Apps can avoid this by aligning their
data appropriately, or using a different GPU backend than Direct3D 12.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

