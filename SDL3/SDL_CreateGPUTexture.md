###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGPUTexture

Creates a texture object to be used in graphics or compute workflows.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTexture* SDL_CreateGPUTexture(
    SDL_GPUDevice *device,
    SDL_GPUTextureCreateInfo *textureCreateInfo);
```

## Function Parameters

|                                                        |                       |                                                         |
| ------------------------------------------------------ | --------------------- | ------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                       | **device**            | a GPU Context.                                          |
| [SDL_GPUTextureCreateInfo](SDL_GPUTextureCreateInfo) * | **textureCreateInfo** | a struct describing the state of the texture to create. |

## Return Value

([SDL_GPUTexture](SDL_GPUTexture) *) Returns a texture object on success,
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

- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)
- [SDL_BindGPUVertexSamplers](SDL_BindGPUVertexSamplers)
- [SDL_BindGPUVertexStorageTextures](SDL_BindGPUVertexStorageTextures)
- [SDL_BindGPUFragmentSamplers](SDL_BindGPUFragmentSamplers)
- [SDL_BindGPUFragmentStorageTextures](SDL_BindGPUFragmentStorageTextures)
- [SDL_BindGPUComputeStorageTextures](SDL_BindGPUComputeStorageTextures)
- [SDL_BlitGPUTexture](SDL_BlitGPUTexture)
- [SDL_ReleaseGPUTexture](SDL_ReleaseGPUTexture)
- [SDL_GPUTextureSupportsFormat](SDL_GPUTextureSupportsFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

