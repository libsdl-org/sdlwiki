# SDL_CreateGPUTexture

Creates a texture object to be used in graphics or compute workflows.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUTexture * SDL_CreateGPUTexture(
    SDL_GPUDevice *device,
    const SDL_GPUTextureCreateInfo *createinfo);
```

## Function Parameters

|                                                              |                |                                                         |
| ------------------------------------------------------------ | -------------- | ------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *                             | **device**     | a GPU Context.                                          |
| const [SDL_GPUTextureCreateInfo](SDL_GPUTextureCreateInfo) * | **createinfo** | a struct describing the state of the texture to create. |

## Return Value

([SDL_GPUTexture](SDL_GPUTexture) *) Returns a texture object on success,
or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The contents of this texture are undefined until data is written to the
texture.

Note that certain combinations of usage flags are invalid. For example, a
texture cannot have both the SAMPLER and GRAPHICS_STORAGE_READ flags.

If you request a sample count higher than the hardware supports, the
implementation will automatically fall back to the highest available sample
count.

There are optional properties that can be provided through
[SDL_GPUTextureCreateInfo](SDL_GPUTextureCreateInfo)'s `props`. These are
the supported properties:

- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_R_FLOAT`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_R_FLOAT):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_COLOR_TARGET](SDL_GPU_TEXTUREUSAGE_COLOR_TARGET),
  clear the texture to a color with this red intensity. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_G_FLOAT`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_G_FLOAT):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_COLOR_TARGET](SDL_GPU_TEXTUREUSAGE_COLOR_TARGET),
  clear the texture to a color with this green intensity. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_B_FLOAT`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_B_FLOAT):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_COLOR_TARGET](SDL_GPU_TEXTUREUSAGE_COLOR_TARGET),
  clear the texture to a color with this blue intensity. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_A_FLOAT`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_A_FLOAT):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_COLOR_TARGET](SDL_GPU_TEXTUREUSAGE_COLOR_TARGET),
  clear the texture to a color with this alpha intensity. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_DEPTH_FLOAT`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_DEPTH_FLOAT):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET](SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET),
  clear the texture to a depth of this value. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_STENCIL_UINT8`](SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_STENCIL_UINT8):
  (Direct3D 12 only) if the texture usage is
  [SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET](SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET),
  clear the texture to a stencil of this value. Defaults to zero.
- [`SDL_PROP_GPU_TEXTURE_CREATE_NAME_STRING`](SDL_PROP_GPU_TEXTURE_CREATE_NAME_STRING):
  a name that can be displayed in debugging tools.

## Version

This function is available since SDL 3.2.0.

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

