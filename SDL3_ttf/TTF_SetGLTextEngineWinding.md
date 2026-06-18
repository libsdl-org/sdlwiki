###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetGLTextEngineWinding

Sets the winding order of the vertices returned by [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData) for a particular GL text engine.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetGLTextEngineWinding(TTF_TextEngine *engine, TTF_GLTextEngineWinding winding);
```

## Function Parameters

|                                                    |             |                                                                                                            |
| -------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------- |
| [TTF_TextEngine](TTF_TextEngine) *                 | **engine**  | a [TTF_TextEngine](TTF_TextEngine) object created with [TTF_CreateGLTextEngine](TTF_CreateGLTextEngine)(). |
| [TTF_GLTextEngineWinding](TTF_GLTextEngineWinding) | **winding** | the new winding order option.                                                                              |

## Thread Safety

This function should be called on the thread that created the engine.

## Version

This function is available since SDL_ttf 3.3.0.

## See Also

- [TTF_GetGLTextEngineWinding](TTF_GetGLTextEngineWinding)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

