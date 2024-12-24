###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGPUTextEngineWinding

Get the winding order of the vertices returned by [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData) for a particular GPU text engine

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_GPUTextEngineWinding TTF_GetGPUTextEngineWinding(const TTF_TextEngine *engine);
```

## Function Parameters

|                                          |            |                                                                                                              |
| ---------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| const [TTF_TextEngine](TTF_TextEngine) * | **engine** | a [TTF_TextEngine](TTF_TextEngine) object created with [TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)(). |

## Return Value

([TTF_GPUTextEngineWinding](TTF_GPUTextEngineWinding)) Returns the winding
order used by the GPU text engine or
[TTF_GPU_TEXTENGINE_WINDING_INVALID](TTF_GPU_TEXTENGINE_WINDING_INVALID) in
case of error.

## Thread Safety

This function should be called on the thread that created the engine.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetGPUTextEngineWinding](TTF_SetGPUTextEngineWinding)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

