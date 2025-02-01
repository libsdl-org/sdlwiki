###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateRendererTextEngineWithProperties

Create a text engine for drawing text on an SDL renderer, with the specified properties.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateRendererTextEngineWithProperties(SDL_PropertiesID props);


#define TTF_PROP_RENDERER_TEXT_ENGINE_RENDERER                 "SDL_ttf.renderer_text_engine.create.renderer"
#define TTF_PROP_RENDERER_TEXT_ENGINE_ATLAS_TEXTURE_SIZE       "SDL_ttf.renderer_text_engine.create.atlas_texture_size"
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

- [`TTF_PROP_RENDERER_TEXT_ENGINE_RENDERER`](TTF_PROP_RENDERER_TEXT_ENGINE_RENDERER):
  the renderer to use for creating textures and drawing text
- [`TTF_PROP_RENDERER_TEXT_ENGINE_ATLAS_TEXTURE_SIZE`](TTF_PROP_RENDERER_TEXT_ENGINE_ATLAS_TEXTURE_SIZE):
  the size of the texture atlas

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateRendererTextEngine](TTF_CreateRendererTextEngine)
- [TTF_DestroyRendererTextEngine](TTF_DestroyRendererTextEngine)
- [TTF_DrawRendererText](TTF_DrawRendererText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

