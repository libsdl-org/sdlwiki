###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetGPUTextEngineWinding

Sets the winding order of the vertices returned by [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData) for a particular GPU text engine.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetGPUTextEngineWinding(TTF_TextEngine *engine, TTF_GPUTextEngineWinding winding);
```

## Function Parameters

|                                                      |             |                                                                                                              |
| ---------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| [TTF_TextEngine](TTF_TextEngine) *                   | **engine**  | a [TTF_TextEngine](TTF_TextEngine) object created with [TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)(). |
| [TTF_GPUTextEngineWinding](TTF_GPUTextEngineWinding) | **winding** | the new winding order option.                                                                                |

## Thread Safety

This function should be called on the thread that created the engine.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetGPUTextEngineWinding](TTF_GetGPUTextEngineWinding)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

