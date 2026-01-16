###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadGPUTexture

Load an image from a filesystem path into a GPU texture.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_GPUTexture * IMG_LoadGPUTexture(SDL_GPUDevice *device, SDL_GPUCopyPass *copy_pass, const char *file, int *width, int *height);
```

## Function Parameters

|                   |               |                                                                           |
| ----------------- | ------------- | ------------------------------------------------------------------------- |
| SDL_GPUDevice *   | **device**    | the SDL_GPUDevice to use to create the GPU texture.                       |
| SDL_GPUCopyPass * | **copy_pass** | the SDL_GPUCopyPass to use to upload the loaded image to the GPU texture. |
| const char *      | **file**      | a path on the filesystem to load an image from.                           |
| int *             | **width**     | a pointer filled in with the width of the GPU texture. may be NULL.       |
| int *             | **height**    | a pointer filled in with the width of the GPU texture. may be NULL.       |

## Return Value

(SDL_GPUTexture *) Returns a new GPU texture, or NULL on error.

## Remarks

An SDL_GPUTexture represents an image in GPU memory, usable by SDL's GPU
API. Regardless of the source format of the image, this function will
create a GPU texture with the format SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM
with no mip levels. It can be bound as a sampled texture from a graphics or
compute pipeline and as a a readonly storage texture in a compute pipeline.

There is a separate function to read files from an SDL_IOStream, if you
need an i/o abstraction to provide data from anywhere instead of a simple
filesystem read; that function is
[IMG_LoadGPUTexture_IO](IMG_LoadGPUTexture_IO)().

When done with the returned texture, the app should dispose of it with a
call to SDL_ReleaseGPUTexture().

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_LoadGPUTextureTyped_IO](IMG_LoadGPUTextureTyped_IO)
- [IMG_LoadGPUTexture_IO](IMG_LoadGPUTexture_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

