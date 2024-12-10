###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGPUTextDrawData

Get the geometry data needed for drawing the text.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_GPUAtlasDrawSequence* TTF_GetGPUTextDrawData(TTF_Text *text);
```

## Function Parameters

|                        |          |                   |
| ---------------------- | -------- | ----------------- |
| [TTF_Text](TTF_Text) * | **text** | the text to draw. |

## Return Value

([TTF_GPUAtlasDrawSequence](TTF_GPUAtlasDrawSequence) *) Returns a NULL
terminated linked list of
[TTF_GPUAtlasDrawSequence](TTF_GPUAtlasDrawSequence) objects or NULL if the
passed text is empty or in case of failure; call SDL_GetError() for more
information.

## Remarks

`text` must have been created using a [TTF_TextEngine](TTF_TextEngine) from
[TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)().

If the text looks blocky use linear filtering.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)
- [TTF_CreateText](TTF_CreateText)
- [TTF_CreateText_Wrapped](TTF_CreateText_Wrapped)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

