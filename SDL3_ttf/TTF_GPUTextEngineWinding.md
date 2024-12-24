###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GPUTextEngineWinding

The winding order of the vertices returned by [TTF_GetGPUTextDrawData](TTF_GetGPUTextDrawData)

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef enum TTF_GPUTextEngineWinding
{
    TTF_GPU_TEXTENGINE_WINDING_INVALID = -1,
    TTF_GPU_TEXTENGINE_WINDING_CLOCKWISE,
    TTF_GPU_TEXTENGINE_WINDING_COUNTER_CLOCKWISE
} TTF_GPUTextEngineWinding;
```

## Version

This enum is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLTTF](CategorySDLTTF)

