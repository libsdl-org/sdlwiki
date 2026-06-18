###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateGLTextEngineWithProperties

Create a text engine for drawing text with OpenGL, with extra properties.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateGLTextEngineWithProperties(SDL_PropertiesID props);


#define TTF_PROP_GL_TEXT_ENGINE_ATLAS_TEXTURE_SIZE_NUMBER "SDL_ttf.gl_text_engine.create.atlas_texture_size"
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

The caller is responsible for ensuring the correct OpenGL context is
current when calling this function and when using the resulting text
engine.

The following properties are supported:

- [`TTF_PROP_GL_TEXT_ENGINE_ATLAS_TEXTURE_SIZE_NUMBER`](TTF_PROP_GL_TEXT_ENGINE_ATLAS_TEXTURE_SIZE_NUMBER):
  the size of the texture atlas in pixels, defaults to 1024.

## Thread Safety

This function should be called on the thread that created the OpenGL
context.

## Version

This function is available since SDL_ttf 3.3.0.

## See Also

- [TTF_CreateGLTextEngine](TTF_CreateGLTextEngine)
- [TTF_DestroyGLTextEngine](TTF_DestroyGLTextEngine)
- [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

