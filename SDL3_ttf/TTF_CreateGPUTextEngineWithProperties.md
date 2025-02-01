###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateGPUTextEngineWithProperties

Create a text engine for drawing text with the SDL GPU API, with the specified properties.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateGPUTextEngineWithProperties(SDL_PropertiesID props);


#define TTF_PROP_GPU_TEXT_ENGINE_DEVICE                   "SDL_ttf.gpu_text_engine.create.device"
#define TTF_PROP_GPU_TEXT_ENGINE_ATLAS_TEXTURE_SIZE       "SDL_ttf.gpu_text_engine.create.atlas_texture_size"
```

## Function Parameters

|                  |           |                        |
| ---------------- | --------- | ---------------------- |
| SDL_PropertiesID | **props** | the properties to use. |

## Return Value

([TTF_TextEngine](TTF_TextEngine) *) Returns a
[TTF_TextEngine](TTF_TextEngine) object or NULL on failure; call
SDL_GetError() for more information.

## Remarks

These are the supported properties:

- [`TTF_PROP_GPU_TEXT_ENGINE_DEVICE`](TTF_PROP_GPU_TEXT_ENGINE_DEVICE): the
  SDL_GPUDevice to use for creating textures and drawing text.
- [`TTF_PROP_GPU_TEXT_ENGINE_ATLAS_TEXTURE_SIZE`](TTF_PROP_GPU_TEXT_ENGINE_ATLAS_TEXTURE_SIZE):
  the size of the texture atlas

## Thread Safety

This function should be called on the thread that created the device.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)
- [TTF_DestroyGPUTextEngine](TTF_DestroyGPUTextEngine)
- [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

