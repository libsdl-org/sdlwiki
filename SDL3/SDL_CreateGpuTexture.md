###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuTexture

Creates a texture object to be used in graphics or compute workflows.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuTexture* SDL_CreateGpuTexture(
    SDL_GpuDevice *device,
    SDL_GpuTextureCreateInfo *textureCreateInfo);
```

## Function Parameters

|                                                        |                       |                                                         |
| ------------------------------------------------------ | --------------------- | ------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *                       | **device**            | a GPU Context.                                          |
| [SDL_GpuTextureCreateInfo](SDL_GpuTextureCreateInfo) * | **textureCreateInfo** | a struct describing the state of the texture to create. |

## Return Value

([SDL_GpuTexture](SDL_GpuTexture) *) Returns a texture object on success,
or NULL on failure.

## Remarks

The contents of this texture are undefined until data is written to the
texture.

Note that certain combinations of usage flags are invalid. For example, a
texture cannot have both the SAMPLER and GRAPHICS_STORAGE_READ flags.

If you request a sample count higher than the hardware supports, the
implementation will automatically fall back to the highest available sample
count.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UploadToGpuTexture](SDL_UploadToGpuTexture)
- [SDL_DownloadFromGpuTexture](SDL_DownloadFromGpuTexture)
- [SDL_BindGpuVertexSamplers](SDL_BindGpuVertexSamplers)
- [SDL_BindGpuVertexStorageTextures](SDL_BindGpuVertexStorageTextures)
- [SDL_BindGpuFragmentSamplers](SDL_BindGpuFragmentSamplers)
- [SDL_BindGpuFragmentStorageTextures](SDL_BindGpuFragmentStorageTextures)
- [SDL_BindGpuComputeStorageTextures](SDL_BindGpuComputeStorageTextures)
- [SDL_BlitGpu](SDL_BlitGpu)
- [SDL_ReleaseGpuTexture](SDL_ReleaseGpuTexture)
- [SDL_SupportsGpuTextureFormat](SDL_SupportsGpuTextureFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

