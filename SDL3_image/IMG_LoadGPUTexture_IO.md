###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadGPUTexture_IO

Load an image from an SDL data source into a GPU texture.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_GPUTexture * IMG_LoadGPUTexture_IO(SDL_GPUDevice *device, SDL_GPUCopyPass *copy_pass, SDL_IOStream *src, bool closeio, int *width, int *height);
```

## Function Parameters

|                   |               |                                                                               |
| ----------------- | ------------- | ----------------------------------------------------------------------------- |
| SDL_GPUDevice *   | **device**    | the SDL_GPUDevice to use to create the GPU texture.                           |
| SDL_GPUCopyPass * | **copy_pass** | the SDL_GPUCopyPass to use to upload the loaded image to the GPU texture.     |
| SDL_IOStream *    | **src**       | an SDL_IOStream that data will be read from.                                  |
| bool              | **closeio**   | true to close/free the SDL_IOStream before returning, false to leave it open. |
| int *             | **width**     | a pointer filled in with the width of the GPU texture. may be NULL.           |
| int *             | **height**    | a pointer filled in with the width of the GPU texture. may be NULL.           |

## Return Value

(SDL_GPUTexture *) Returns a new GPU texture, or NULL on error.

## Remarks

An SDL_GPUTexture represents an image in GPU memory, usable by SDL's GPU
API. Regardless of the source format of the image, this function will
create a GPU texture with the format SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM
with no mip levels. It can be bound as a sampled texture from a graphics or
compute pipeline and as a a readonly storage texture in a compute pipeline.

If `closeio` is true, `src` will be closed before returning, whether this
function succeeds or not. SDL_image reads everything it needs from `src`
during this call in any case.

There is a separate function to read files from disk without having to deal
with SDL_IOStream: `[IMG_LoadGPUTexture](IMG_LoadGPUTexture)(device,
copy_pass, "filename.jpg", width, height) will call this function and
manage those details for you, determining the file type from the filename's
extension.

There is also [IMG_LoadGPUTextureTyped_IO](IMG_LoadGPUTextureTyped_IO)(),
which is equivalent to this function except a file extension (like "BMP",
"JPG", etc) can be specified, in case SDL_image cannot autodetect the file
format.

When done with the returned texture, the app should dispose of it with a
call to SDL_ReleaseGPUTexture().

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_LoadGPUTexture](IMG_LoadGPUTexture)
- [IMG_LoadGPUTextureTyped_IO](IMG_LoadGPUTextureTyped_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

