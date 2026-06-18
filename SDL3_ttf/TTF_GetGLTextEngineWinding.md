###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGLTextEngineWinding

Get the winding order of the vertices returned by [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData) for a particular GL text engine.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_GLTextEngineWinding TTF_GetGLTextEngineWinding(const TTF_TextEngine *engine);
```

## Function Parameters

|                                          |            |                                                                                                            |
| ---------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| const [TTF_TextEngine](TTF_TextEngine) * | **engine** | a [TTF_TextEngine](TTF_TextEngine) object created with [TTF_CreateGLTextEngine](TTF_CreateGLTextEngine)(). |

## Return Value

([TTF_GLTextEngineWinding](TTF_GLTextEngineWinding)) Returns the winding
order used by the GL text engine or
[TTF_GL_TEXTENGINE_WINDING_INVALID](TTF_GL_TEXTENGINE_WINDING_INVALID) in
case of error.

## Thread Safety

This function should be called on the thread that created the engine.

## Version

This function is available since SDL_ttf 3.3.0.

## See Also

- [TTF_SetGLTextEngineWinding](TTF_SetGLTextEngineWinding)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

